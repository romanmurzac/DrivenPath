# **Chapter 3:** Batch processing - *Local Pipeline*

## Scenario
For third Chapter / Sprint needs to create orchestrated pipeline that will allow to run all stages in managed way. The pipeline should run daily and make data available at 08:00 AM. The pipeline should extract data into bronze layer (raw zone) named *driven_raw*, apply necessary transformations into silver layer (staging zone) named *driven_staging*, and upload data to the golden layer (trusted zone) named *driven_trusted* for consumtion in analytical process. It required in golden layer to have four tables: financial table for payment calculation, technical table for technical issue analyze, non-pii table for access for all users with limited access level across the organization, and pii table for users with high access level.

## Assignment
For current Sprint / Chapter your tasks are:
1. **Read** from [Theory](#theory) section about:\
    a. Docker:
    * i. Docker.
    * ii. Docker compose.
    * iii. Docker Desktop.
    * iv. Docker Hub.

    b. Airflow:
    * i. Airflow.
    * ii. Airflow DAG.
    * iii. Airflow operators.

    c. dbt.

2. **Implement** from [Practice](#practice) section for *DataDriven* company:\.\
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
    * iii. Setup Connetion.
    * iv. Create DAG.
    * v. Run DAG.

    d. Setup pgAdmin 4 database:
    * i. Connect to database.
    * ii. Check data in pipeline.

3. **Work** for *LeadData* company on Sprint / Chapter tasks:\
**Note:** For point 3 (*Work*) implementation, read current part for individual scenario from `work_3/scenario_3.md` file and put all your work evidences in `work_3` directory.

## Theory
Main theoretical notions of the chapter with proper resources for self paced learning.

### Docker
#### Description
Docker is a software platform that allows you to build, test, and deploy applications quickly. Docker packages software into standardized units called containers that have everything the software needs to run including libraries, system tools, code, and runtime. Using Docker, you can quickly deploy and scale applications into any environment and know your code will run.
#### References
[Docker Curriculum - A Docker Tutorial for Beginners](https://docker-curriculum.com/)\
[IBM - What is Docker?](https://www.ibm.com/topics/docker)\
[AWS - What is Docker?](https://aws.amazon.com/docker/)

### Docker compose
#### Description
Docker Compose is a tool for running multi-container applications on Docker defined using the Compose file format. A Compose file is used to define how one or more containers that make up your application are configured. Once you have a Compose file, you can create and start your application with a single command: docker compose up.
#### References
[GitHub - Docker compose](https://github.com/docker/compose)\
[Docker docs - Docker Compose overview](https://docs.docker.com/compose/)\
[TutorialsPoint - Docker - Compose](https://www.tutorialspoint.com/docker/docker_compose.htm)

### Docker Desktop
#### Description
Docker Desktop is a one-click-install application for your Mac, Linux, or Windows environment that lets you build, share, and run containerized applications and microservices.
It provides a straightforward GUI (Graphical User Interface) that lets you manage your containers, applications, and images directly from your machine.
Docker Desktop reduces the time spent on complex setups so you can focus on writing code. It takes care of port mappings, file system concerns, and other default settings, and is regularly updated with bug fixes and security updates.
#### References
[Docker docs - Install Docker Desktop](https://docs.docker.com/desktop/install/windows-install/)\
[Docker docs - Overview of Docker Desktop](https://docs.docker.com/desktop/)

### Docker Hub
#### Description
Docker Hub is a container registry built for developers and open source contributors to find, use, and share their container images. With Hub, developers can host public repos that can be used for free, or private repos for teams and enterprises.
#### References
[Docker Hub](https://hub.docker.com/)\
[Docker docs - Overview of Docker Hub](https://docs.docker.com/docker-hub/)

### Airflow
#### Description
Apache Airflow (or simply Airflow) is a platform to programmatically author, schedule, and monitor workflows.
When workflows are defined as code, they become more maintainable, versionable, testable, and collaborative.
Use Airflow to author workflows as directed acyclic graphs (DAGs) of tasks. The Airflow scheduler executes your tasks on an array of workers while following the specified dependencies. Rich command line utilities make performing complex surgeries on DAGs a snap. The rich user interface makes it easy to visualize pipelines running in production, monitor progress, and troubleshoot issues when needed.
#### References
[GitHub - Apache Airflow](https://github.com/apache/airflow)\
[Run AI - Apache Airflow
Use Cases, Architecture, and Best Practices](https://www.run.ai/guides/machine-learning-operations/apache-airflow#:~:text=Apache%20Airflow%20is%20an%20open,be%20easily%20scheduled%20and%20monitored.)\
[Apache Airflow](https://airflow.apache.org/)

### Airflow DAG
#### Description
In Airflow, a DAG – or a Directed Acyclic Graph – is a collection of all the tasks you want to run, organized in a way that reflects their relationships and dependencies. A DAG is defined in a Python script, which represents the DAGs structure (tasks and their dependencies) as code.
#### References
[Apache Airflow - DAGs](https://airflow.apache.org/docs/apache-airflow/stable/core-concepts/dags.html)\
[Medium - Creating a DAG in Apache Airflow for Beginners: A Comprehensive Guide](https://medium.com/apache-airflow/creating-a-dag-in-apache-airflow-for-beginners-a-comprehensive-guide-30a61cf61bea)\
[Medium - Avoiding the pitfalls of top-level DAG code](https://medium.com/apache-airflow/avoiding-the-pitfalls-of-top-level-dag-code-fa480d9e75c6)

### Airflow operators
#### Description
Operators are the building blocks of Airflow DAGs. They contain the logic of how data is processed in a pipeline. Each task in a DAG is defined by instantiating an operator.
There are many different types of operators available in Airflow. Some operators such as Python functions execute general code provided by the user, while other operators perform very specific actions such as transferring data from one system to another.
#### References
[Apache Airflow - Operators](https://airflow.apache.org/docs/apache-airflow/stable/core-concepts/operators.html)\
[Astronomer - Airflow operators](https://www.astronomer.io/docs/learn/what-is-an-operator)

### dbt
#### Description
dbt (data build tool) makes data engineering activities accessible to people with data analyst skills to transform the data in the warehouse using simple select statements, effectively creating your entire transformation process with code.
#### References
[dbt](https://www.getdbt.com/)\
[Analytics8 - dbt (Data Build Tool) Overview: What is dbt and What Can It Do for My Data Pipeline?](https://www.analytics8.com/blog/dbt-overview-what-is-dbt-and-what-can-it-do-for-my-data-pipeline/#:~:text=dbt%20(data%20build%20tool)%20makes,entire%20transformation%20process%20with%20code.)\
[Medium - The Power of Data Build Tool (dbt)](https://medium.com/@nydas/the-power-of-data-build-tool-dbt-6b26dfab5bac)

## Practice
Implemention for the practical part of the chapter.

### Setup Docker container
The ETL was developed on local machine named *testing environment* in our case. After local prototying of the ETL process is done, validate with the stakeholders that the actual results match expected results.
In this chapter the *testing environment* processes will be transfered to the *development environment*, also local development that use tools for automation, orchestration and management of all processes as a single unit - **pipeline**.

First, ensure that you have all necessary tools from Chapter 1 installed on your local machine.

#### Run Docker Desktop
Run Docker Desktop application.
In Docker Desktop, beside many other options, you should be able to see: Containers, Images, and Volumes options.
All of them at this moment should be empty as there was nothing run yet.
![Image 3.1](../media/image_3.1.PNG)

As here are needed multiple container to hold the whole infrastructure, install [Docker Compose](https://docs.docker.com/compose/install/).\
Open a terminal and navigate to the project directory by changing `<your_path>` with your actual location and open it in VS Code.
```
cd C:\<your_path>\DrivenPath\chapter_3\src_3
code .
```

#### Retrieve Docker Compose file
Retrieve the `docker-compose.yml` file or [copy](https://airflow.apache.org/docs/apache-airflow/2.10.2/docker-compose.yaml) it in a file with the same name.
```
curl -LfO 'https://airflow.apache.org/docs/apache-airflow/2.10.2/docker-compose.yaml'
```
Now you can run the basic Apache Airflow on your local machine.

#### Update Docker Compose file
For current work there is needed to update the `docker-compose.yml` file and create custom image using as a template updated `docker-compose.yml` file.

Existing image is commented (line 52) as the default image will not be used. Custom image will be built (line 53).
To obtain an empty Airflow environment, change `AIRFLOW__CORE__LOAD_EXAMPLES` to `false` (line 62).
Also, need to add `dbt` directory for dbt project (line 80) and `data` directory (line 81) for generated data inside the container.
![Image 3.2](../media/image_3.2.PNG)

It can be created another database, different from database used by Airflow, but it will be use the same database, but the different schemas will be created.
Add port `5433:5432` to expose the database (lines 97-98). Also, need to make `data` directory available in database (line 101).
![Image 3.3](../media/image_3.3.PNG)

Add `dbt` and `data` directories to be created and to be readable in container (lines 242-243).
![Image 3.4](../media/image_3.4.PNG)

Now `docker-compose.yml` file is customized based on project needs.

#### Add requirements
Create a file `requirements.txt` and copy in it the content from below.\
```
dbt-core==1.8.0
dbt-postgres==1.8.2
faker==18.4.0
```

#### Create Dockerfile
As for current project the custom image is needed, create a `Dockerfile` and paste in it the content from below.\
```
# Use the official Airflow image as a template.
FROM apache/airflow:2.10.2

# Switch to airflow user to install packages.
USER airflow

# Copy the requirements file into the container.
COPY requirements.txt .

# Install all dependencies from the requirements file.
RUN pip install -r requirements.txt

# Copy dbt directory into the container.
COPY dbt /opt/airflow/dbt

```

### Create dbt
The SQL queries that were created for *testing environment* can be used for *development environment* as well, but as the project will grow, it will be hard to mentain all the processes inside the database. In order to have a scalable infrastructure for data modelling will be used **dbt**.\
Create a directory with name `dbt` and inside of it make a directory named `models`.
```
mkdir dbt
cd dbt
mkdir models
cd ../
```

#### Create project
In `dbt` directory create a file named `dbt_project.yml` and copy the content from below.
It will create a dbt project named *dbt_driven_data* that will use *default* profile and models from *models* directory.
```
name: 'dbt_driven_data'
version: '1.0'
profile: 'default'
model-paths: ["models"]
```

#### Create profiles
In `dbt` directory create a file named `profiles.yml` and copy the content from below.
It will define the *default* profile used in project with *dev* environment only. Also, here are defined characteristics of the database.
```
default:
  target: dev
  outputs:
    dev:
      type: postgres
      host: postgres
      user: airflow
      password: airflow
      dbname: airflow
      schema: driven
      port: 5432
```

#### Create sources
In `dbt/models` create a file named `source.yml` and copy the content from below. It will create a source of data that can be used by many models - *raw_source*. The *raw_source* will be located in *airflow* database, in *driven_raw* schema, and the table for raw data is *raw_batch_data*.
```
version: 2

sources:
    name: raw_source
    database: airflow
    schema: driven_raw
    tables:
      name: raw_batch_data
```

#### Create models
In `dbt/models` create a file named `staging_dim_address.sql` and copy the content from below.
```
{{ config(
    materialized='table',
    schema='staging',
    alias='dim_address'
) }}

WITH source_data AS (
    SELECT
        unique_id,
        address,
        mac_address,
        ip_address
    FROM
        {{ source('raw_source', 'raw_batch_data') }}
)

SELECT
    *
FROM
    source_data
```

In `dbt/models` create a file named `staging_dim_data.sql` and copy the content from below.
```
{{ config(
    materialized='table',
    schema='staging',
    alias='dim_data'
) }}

WITH source_data AS (
    SELECT
        unique_id,
        accessed_at
    FROM
        {{ source('raw_source', 'raw_batch_data') }}
)

SELECT
    *
FROM
    source_data
```

In `dbt/models` create a file named `staging_dim_finance.sql` and copy the content from below.
```
{{ config(
    materialized='table',
    schema='staging',
    alias='dim_finance'
) }}

WITH source_data AS (
    SELECT
        unique_id,
        iban
    FROM
        {{ source('raw_source', 'raw_batch_data') }}
)

SELECT
    *
FROM
    source_data
```

In `dbt/models` create a file named `staging_dim_person.sql` and copy the content from below.
```
{{ config(
    materialized='table',
    schema='staging',
    alias='dim_person'
) }}

WITH source_data AS (
    SELECT
        unique_id,
        person_name,
        user_name,
        email,
        phone,
        birth_date,
        personal_number
    FROM
        {{ source('raw_source', 'raw_batch_data') }}
)

SELECT
    *
FROM
    source_data
```

In `dbt/models` create a file named `staging_fact_network_usage.sql` and copy the content from below.
```
{{ config(
    materialized='table',
    schema='staging',
    alias='fact_network_usage'
) }}

WITH source_data AS (
    SELECT
        unique_id,
        session_duration,
        download_speed,
        upload_speed,
        consumed_traffic
    FROM
        {{ source('raw_source', 'raw_batch_data') }}
)

SELECT
    *
FROM
    source_data
```