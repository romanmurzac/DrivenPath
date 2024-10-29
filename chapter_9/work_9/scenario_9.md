## Scenario 9
For ninth Chapter / Sprint it is required to process on daily basis data from previous week from datalake that is stored in S3 bucket and process data by filtering and aggregating and also add aditional columns based on existing ones. After transformations it is required to write data back to the *LeadData* datalake.

## Instructions 9
Use directory `chapter_9/work_9/` as your project directory for work related to the **Chapter 9** for **LeadData** company.

## Assignment 9
a. Develop local pipeline:
* i. Intro Google Colab Notebook.
* ii. Initialize PySpark Session.
* iii. Data Processing.
* iv. Data Analysis.
* v. Validate transformed data.

b. Develop cloud pipeline:
* i. Check raw data.
* ii. Create IAM role.
* iii. Create Glue job.
* iv. Run Glue job.
* v. Validate transformed data.