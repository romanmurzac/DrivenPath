import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job

args = getResolvedOptions(sys.argv, ['JOB_NAME'])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)

# Load data from S3.
datasource = glueContext.create_dynamic_frame.from_catalog(database="driven_data_db", table_name="raw")

# Convert DynamicFrame to DataFrame.
df = datasource.toDF()

# Create a temporary view to run SQL queries.
df.createOrReplaceTempView("raw_data")

# Transform the data.
sql_query = """
SELECT 
    unique_id,
    person_name,
    user_name,
    email,
    phone,
    birth_date,
    personal_number
FROM raw_data
"""

# Execute the SQL query.
transformed_data = spark.sql(sql_query)

# Write the transformed DataFrame back to S3.
transformed_data.write.csv("s3://driven-data-bucket/data/staging/dim_person", header=True, mode="overwrite")

# Commit the actions.
job.commit()
