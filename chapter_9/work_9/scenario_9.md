## Scenario 9
For the ninth chapter/sprint, it is required to process, on a daily basis, the data from the previous week stored in the data lake in the S3 bucket. The processing should involve filtering and aggregating the data, as well as adding additional columns based on existing ones. After the transformations, the processed data must be written back to the *LeadData* data lake.

## Instructions 9
Use the directory `chapter_9/work_9/` as your project directory for work related to **Chapter 9** for **LeadData** company.

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