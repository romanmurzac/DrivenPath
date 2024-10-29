## Scenario 3
For the third chapter/sprint, you need to create an orchestrated pipeline that will allow all stages to run in a managed way. The pipeline should run daily and make data available at 10:00 AM EET. It should extract data into the bronze layer (raw zone) named *lead_raw*, apply necessary transformations into the silver layer (staging zone) named *lead_staging*, and upload data to the golden layer (trusted zone) named *lead_trusted* for consumption in the analytical process. It is required that the golden layer contains four tables: a financial table for payment calculations, a technical table for analyzing technical issues, a non-PII table for access by all users with limited access levels across the organization, and a PII table for users with high access levels.

## Instructions 3
Use the directory `chapter_3/work_3/` as your project directory for work related to **Chapter 3** for **LeadData** company.

## Assignment 3
a. Setup Docker container:
* i. Run Docker Desktop.
* ii. Retrieve Docker Compose file.
* iii. Update Docker Compose file.
* iv. Add requirements.
* v. Create Dockerfile.

b. Create dbt:
* i. Create project.
* ii. Create profiles.
* iii. Create sources.
* iv. Create models.

c. Create Airflow:
* i. Run containers.
* ii. Login.
* iii. Setup Connection.
* iv. Create DAG.
* v. Run DAG.

d. Setup pgAdmin 4 database:
* i. Connect to database.
* ii. Check data in database.