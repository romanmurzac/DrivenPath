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
    a. Setup Docker container.\
    b. Create local Airflow.\
    c. Create sample Airflow DAG.\
    d. Setup Airflow connection.\
    e. Setup pgAdmin 4 database.\
    f. Create Dockerfile.\
    g. Create Airflow DAG.\
    h. Create dbt model.\
    i. Deploy orchestrated pipeline:
    * i. Extract data.
    * ii. Transform data.
    * iii. Load data.
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
