## Scenario 2
For second Chapter / Sprint needs to investigate the data source for *LeadData*, understand the amount of data from previous months, identify available fields and data types. Prepare local ETL pipeline to extract data into bronze layer (raw zone), apply necessary transformations into silver layer (staging zone), and upload data to the golden layer (trusted zone) for consumtion in analytical process. It required in golden layer to have four tables: financial table for payment calculation, technical table for technical issue analyze, non-pii table for access for all users with limited access level across the organization, and pii table for users with high access level.

## Instructions 2
Use directory `chapter_2/work_2/` as your project directory for work related to the **Chapter 2** for **LeadData** company.

## Assignment 2
a. Investigate data source.\
b. Extract data:
* i. Data generator.
* ii. Data extraction.

c. Transform data:
* i. Bronze layer.
* ii. Silver layer.

d. Load data:
* i. Financial Data.
* ii. Support Data.
* iii. Non-PII Data.
* iv. PII Data.