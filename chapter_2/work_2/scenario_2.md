## Scenario 2
For the second chapter/sprint, you need to investigate the data source for *LeadData*, understand the amount of data from the previous months, and identify available fields and data types. Prepare a local ETL pipeline to extract data into the bronze layer (raw zone), apply necessary transformations into the silver layer (staging zone), and upload data to the golden layer (trusted zone) for consumption in the analytical process. It is required that the golden layer contains four tables: a financial table for payment calculations, a technical table for analyzing technical issues, a non-PII table for access by all users with limited access levels across the organization, and a PII table for users with high access levels.

## Instructions 2
Use the directory `chapter_2/work_2/` as your project directory for work related to **Chapter 2** for **LeadData** company.

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