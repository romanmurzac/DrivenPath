## Scenario 3
For third Chapter / Sprint needs to create orchestrated pipeline that will allow to run all stages in managed way. The pipeline should run daily and make data available at 10:00 AM EET. The pipeline should extract data into bronze layer (raw zone) named *lead_raw*, apply necessary transformations into silver layer (staging zone) named *lead_staging*, and upload data to the golden layer (trusted zone) named *lead_trusted* for consumtion in analytical process. It required in golden layer to have four tables: financial table for payment calculation, technical table for technical issue analyze, non-pii table for access for all users with limited access level across the organization, and pii table for users with high access level.

## Instructions 3
Use directory `chapter_3/work_3/` as your project directory for work related to the **Chapter 3** for **LeadData** company.

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