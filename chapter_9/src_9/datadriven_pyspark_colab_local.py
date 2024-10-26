# Import PySpark
import os

from pyspark.context import SparkContext
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, expr, to_date, when, regexp_replace
from pyspark.sql.types import IntegerType, DateType

os.environ["JAVA_HOME"] = "/usr/lib/jvm/java-8-openjdk-amd64"

# Initialize PySpark Session.
sc = SparkContext.getOrCreate()
spark = SparkSession.builder.appName(
	'DrivenData Distributed Computing').getOrCreate()

# Import Data.
df_14 = spark.read.csv('batch_2024-09-14.csv', header=True, inferSchema=True)
df_15 = spark.read.csv('batch_2024-09-15.csv', header=True, inferSchema=True)

# Data Join.
df = df_14.union(df_15)

# Show the schema of the dataset.
df.printSchema()

# Display the first 5 rows.
df.show(5)

# Display dataset summary.
df.describe().show()

# Handle missing values.
df = df.na.fill({"email": "unknown@example.com", "phone": "000-000-0000"})

# Remove duplicates.
df = df.dropDuplicates(subset=["unique_id"])

# Cast datatypes.
df = df.withColumn("birth_date", col("birth_date").cast(DateType()))
df = df.withColumn(
    "session_duration", col("session_duration").cast(IntegerType()))

# Data Filtering.
df_filtered = df.filter(to_date(df.accessed_at) > '2024-10-13')
df_filtered = df.filter(df.consumed_traffic > 1000)

# Grouping and Aggregation.
df_grouped = df.groupBy("person_name").agg(
    {"session_duration": "avg", "consumed_traffic": "sum"})
df_grouped.show()

# Calculate total bandwidth.
df = df.withColumn(
    "total_bandwidth", col("download_speed") + col("upload_speed"))

# Extract birth year.
df = df.withColumn("birth_year", expr("year(birth_date)"))

# Data Segmentation.
df = df.withColumn("activity_level",
                   when(col("session_duration") > 120, "active")
                   .when(col("session_duration").between(30, 120), "moderate")
                   .otherwise("less_active"))

# Data Anonymization.
df = df.withColumn("masked_email",
                   regexp_replace("email", "(\\w{3})\\w+@(\\w+)", "$1***@$2"))

# Average session duration.
df.agg({"session_duration": "avg"}).show()

# Maximum session duration.
df.agg({"session_duration": "max"}).show()

# Network Analysis.
df_ip_activity = df.groupBy("ip_address").agg(
    {"consumed_traffic": "sum"}).orderBy(
        "sum(consumed_traffic)", ascending=False)
df_ip_activity.show()

# Time Series Analysis.
df_time = df.withColumn("access_date",
                        to_date("accessed_at")).groupBy("access_date").count()
df_time.show()

# Export Data.
df.write.csv("processed_data_2024-10-15.csv", header=True)
