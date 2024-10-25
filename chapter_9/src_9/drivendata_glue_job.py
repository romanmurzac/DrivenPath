import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from awsglue.dynamicframe import DynamicFrame
from pyspark.sql.functions import col, to_date, when, regexp_replace, expr
from pyspark.sql.types import IntegerType, DateType

# Parse job parameters.
args = getResolvedOptions(sys.argv, ['JOB_NAME'])

# Initialize Spark and Glue context.
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

# Step 1: Read the input CSV from S3 into a DynamicFrame.
input_path = "s3://driven-data-bucket/raw_data/"
dynamic_frame = glueContext.create_dynamic_frame.from_options(
    connection_type="s3",
    connection_options={"paths": [input_path]},
    format="csv",
    format_options={"withHeader": True}
)

# Convert DynamicFrame to DataFrame for transformations.
df = dynamic_frame.toDF()

# Step 2: Data Cleaning and Transformation.
# Fill missing values for 'email' and 'phone'.
df = df.na.fill({"email": "unknown@example.com", "phone": "000-000-0000"})

# Cast birth_date and session_duration to correct types.
df = df.withColumn("birth_date", col("birth_date").cast(DateType()))
df = df.withColumn("session_duration", col("session_duration").cast(IntegerType()))

# Remove duplicates based on 'unique_id'.
df = df.dropDuplicates(subset=["unique_id"])

# Filter based on session duration and accessed_at date.
df_filtered = df.filter((df["session_duration"] > 30) & (to_date(df["accessed_at"]) > "2024-01-01"))

# Create new column for total_bandwidth (download_speed + upload_speed).
df_filtered = df_filtered.withColumn("total_bandwidth", col("download_speed") + col("upload_speed"))

# Create segments based on session_duration (active, moderate, less_active).
df_filtered = df_filtered.withColumn("activity_level", when(col("session_duration") > 120, "active")
                                              .when(col("session_duration").between(30, 120), "moderate")
                                              .otherwise("less_active"))

# Mask email addresses for privacy.
df_filtered = df_filtered.withColumn("masked_email", regexp_replace("email", "(\\w{3})\\w+@(\\w+)", "$1***@$2"))

# Perform some aggregation (group by 'person_name' and calculate average session duration).
df_grouped = df_filtered.groupBy("person_name").agg({"session_duration": "avg", "consumed_traffic": "sum"})

# Step 3: Convert back to DynamicFrame for Glue to process.
filtered_dynamic_frame = DynamicFrame.fromDF(df_filtered, glueContext, "filtered_dynamic_frame")
grouped_dynamic_frame = DynamicFrame.fromDF(df_grouped, glueContext, "grouped_dynamic_frame")

# Step 4: Write the processed data back to S3.
output_path = "s3://driven-data-bucket/transformed_data/"

# Write filtered data to S3.
glueContext.write_dynamic_frame.from_options(
    frame=filtered_dynamic_frame,
    connection_type="s3",
    connection_options={"path": output_path + "filtered/"},
    format="csv",
    format_options={"header": True}
)

# Write grouped data to S3.
glueContext.write_dynamic_frame.from_options(
    frame=grouped_dynamic_frame,
    connection_type="s3",
    connection_options={"path": output_path + "grouped/"},
    format="csv",
    format_options={"header": True}
)

# Step 5: Commit the job.
job.commit()
