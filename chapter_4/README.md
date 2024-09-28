# **Chapter 4:** Batch processing - *Cloud: Console pipeline*

## Scenario
For fourth Chapter / Sprint needs to consolidate the pipeline that was developed on local machine, optimize pipeline processes, create the Cloud Architecture for the product to be robust and scalable, implement proposed architecture via Console to the AWS Cloud, validate in Cloud the *DataDriven* pipeline.

## Assignment
For current Sprint / Chapter your tasks are:
1. **Read** from [Theory](#theory) section about:\
    a. Amazon Web Services:
    * i. S3.
    * ii. IAM.
    * iii. MWAA.
    * iv. Glue job.
    * v. Crawler.
    * vi. Athena.
    * vii. VPC.

2. **Implement** from [Practice](#practice) section for *DataDriven* company:\
    a. Setup AWS Console:
    * i. Login to AWS.
    * ii. Setup Console.

    b. Setup Services:
    * i. S3.
    * ii. VPC.
    * iii. MWAA.
    * iv. IAM.

    c. Run DAG:
    * i. Create DAG.
    * ii. Address IAM restrictions.
    * iii. Test DAG.
    * iv. Run pipeline via DAG.

    d. Crawl data:
    * i. Create database.
    * ii. Create DataCatalog.
    * iii. Crawl data.

    e. Consume data:
    * i. Access Athena.
    * ii. Query data.

3. **Work** for *LeadData* company on Sprint / Chapter tasks:\
**Note:** For point 3 implementation, read current part of scenario from `scenario_4.md` file and put all your work evidences in `work_4` directory.

## Theory
Main theoretical notions of the chapter with proper resources for self paced learning.

### Simple Storage Service
#### Description
Amazon Simple Storage Service (Amazon S3) is an object storage service that offers industry-leading scalability, data availability, security, and performance. Customers of all sizes and industries can use Amazon S3 to store and protect any amount of data for a range of use cases, such as data lakes, websites, mobile applications, backup and restore, archive, enterprise applications, IoT devices, and big data analytics. Amazon S3 provides management features so that you can optimize, organize, and configure access to your data to meet your specific business, organizational, and compliance requirements.
#### References
[AWS - What is Amazon S3?](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html)\
[TechTarget - Amazon Simple Storage Service (Amazon S3)](https://www.techtarget.com/searchaws/definition/Amazon-Simple-Storage-Service-Amazon-S3)

### Identity Access Management
#### Description
Identity and access management (IAM or IdAM for short) is a way to tell who a user is and what they are allowed to do. IAM is like the bouncer at the door of a nightclub with a list of who is allowed in, who isn't allowed in, and who is able to access the VIP area. IAM is also called identity management (IdM).
#### References
[CloudFlare - What is identity and access management (IAM)?](https://www.cloudflare.com/learning/access-management/what-is-identity-and-access-management/)\
[AWS - AWS Identity and Access Management](https://aws.amazon.com/iam/)

### Managed Workflows for Apache Airflow
#### Description
Amazon Managed Workflows for Apache Airflow is a managed orchestration service for Apache Airflow that you can use to setup and operate data pipelines in the cloud at scale. Apache Airflow is an open-source tool used to programmatically author, schedule, and monitor sequences of processes and tasks referred to as workflows. With Amazon MWAA, you can use Apache Airflow and Python to create workflows without having to manage the underlying infrastructure for scalability, availability, and security. Amazon MWAA automatically scales its workflow execution capacity to meet your needs, Amazon MWAA integrates with AWS security services to help provide you with fast and secure access to your data.
#### References
[AWS - What Is Amazon Managed Workflows for Apache Airflow?](https://docs.aws.amazon.com/mwaa/latest/userguide/what-is-mwaa.html)\
[Boto3 - MWAA](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mwaa.html)

### Glue job
#### Description
AWS Glue is a serverless data integration service that makes it easy for analytics users to discover, prepare, move, and integrate data from multiple sources. You can use it for analytics, machine learning, and application development. It also includes additional productivity and data ops tooling for authoring, running jobs, and implementing business workflows.
#### References
[AWS - What is AWS Glue?](https://docs.aws.amazon.com/glue/latest/dg/what-is-glue.html)\
[AWS - AWS Glue API](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api.html)

### Crawler
#### Description
You can use an AWS Glue crawler to populate the AWS Glue Data Catalog with databases and tables. This is the primary method used by most AWS Glue users. A crawler can crawl multiple data stores in a single run. Upon completion, the crawler creates or updates one or more tables in your Data Catalog. Extract, transform, and load (ETL) jobs that you define in AWS Glue use these Data Catalog tables as sources and targets. The ETL job reads from and writes to the data stores that are specified in the source and target Data Catalog tables.
#### References
[AWS - Using crawlers to populate the Data Catalog](https://docs.aws.amazon.com/glue/latest/dg/add-crawler.html)\
[StackOverflow - What does an AWS Glue Crawler do](https://stackoverflow.com/questions/53608650/what-does-an-aws-glue-crawler-do)

### Athena
#### Description
Amazon Athena is a serverless, interactive analytics service built on open-source frameworks, supporting open-table and file formats. Athena provides a simplified, flexible way to analyze petabytes of data where it lives. Analyze data or build applications from an Amazon Simple Storage Service (S3) data lake and 30 data sources, including on-premises data sources or other cloud systems using SQL or Python. Athena is built on open-source Trino and Presto engines and Apache Spark frameworks, with no provisioning or configuration effort required.
#### References
[AWS - Amazon Athena](https://aws.amazon.com/athena/)\
[CloudZero - What Is AWS Athena? Here’s Everything You Need To Know](https://www.cloudzero.com/blog/aws-athena/)

### Virtual Private Cloud
#### Description
With Amazon Virtual Private Cloud (Amazon VPC), you can launch AWS resources in a logically isolated virtual network that you've defined. This virtual network closely resembles a traditional network that you'd operate in your own data center, with the benefits of using the scalable infrastructure of AWS.
#### References
[AWS - What is Amazon VPC?](https://docs.aws.amazon.com/vpc/latest/userguide/what-is-amazon-vpc.html)\
[GeeksforGeeks - Amazon VPC – Introduction to Amazon Virtual Private Cloud](https://www.geeksforgeeks.org/amazon-vpc-introduction-to-amazon-virtual-cloud/)

## Practice
Implemention for the practical part of the chapter.

### Setup AWS Console
As first interaction with AWS is the Console. Here you can test the services and also, you can test your features that you develop. This will be first approach to prove the concept of the pipeline in cloud.

#### Login to AWS
Access the [AWS Console](https://aws.amazon.com/console) and press `Sign In` button. Use `Root user` option and enter email address that you used to create de AWS account. After email address, on next page, enter the password.
![Image 4.1](../media/image_4.1.PNG)

#### Setup Console
Once you're logged into the AWS account, you'll see the console where you can do actions manually in cloud. This chapter is fully dedicated to manual development via console.
![Image 4.2](../media/image_4.2.PNG)

In the console are available two main options to access the AWS services: click on left panel `Console Home` and choose `All services` and central panel you'll see all services available in AWS Cloud arranged by category. Now you can click on desired services and configure them.
![Image 4.3](../media/image_4.3.PNG)

Also, in order to access a service in AWS Cloud you can just write the name of the service in the `Search` panel and the service will be listed. It is not mandatory to write the full name of the services to get them in list, it works even with abreviations.
![Image 4.4](../media/image_4.4.PNG)

### Setup Services
In order to prove the concept for the pipeline developed for *DrivenData* it will be tested in cloud by setup each component one by one via Console.

#### S3 - Simple Storage Service
First service that will be used is S3 - Simple Storage Service is a storage that is used as datalake. Search or access from the list `S3` and access it. As there no buckets created yet, you should see an empty S3. 
![Image 4.5](../media/image_4.5.PNG)

Presson `Create bucket` provide the name `driven-data-bucket`, keep ACLs disabled. 
![Image 4.6](../media/image_4.6.PNG)

Also, disable `Block all public access`.
![Image 4.7](../media/image_4.7.PNG)

Disable bucket versioning. Choose `SSE-S3` as encryption type. and enable bucket key usage.
![Image 4.8](../media/image_4.8.PNG)

Press `create` and now you should see the bucket `driven-data-bucket` in S3 bucket list.
![Image 4.9](../media/image_4.9.PNG)

Click on bucket name and access it. Inside the bucket press `Upload` option and select `Add files` and choose file from *Chapter 2* - `batch_2024-09-14.csv`.
![Image 4.10](../media/image_4.10.PNG)

#### VPC - Virtual Private Cloud
In order to create the Airflow environment in AWS Cloud it is required to create or use the default Virtual Private Cloud. Search for `VPC` and in VPC options choose `Subnets`. Here you should see three default public subnets. It is needed to create at least two private subnets.\
Press `Create subnet` and in `VPC ID` choose the default VPC.
![Image 4.11](../media/image_4.11.PNG)

Introduce the name of the subnet `private-zone-a`, choose as *Availability Zone* `eu-central-1a` and for *subnet CIDR block* choose the IP `nnn.nn.48.0/20`.\
Create one more subnet with the name `private-zone-b`, choose as *Availability Zone* `eu-central-1b` and for *subnet CIDR block* choose the IP `nnn.nn.64.0/20`.
![Image 4.12](../media/image_4.12.PNG)

Now you should see al five subnets: three default public subnets and two private subnets that were created.
![Image 4.13](../media/image_4.13.PNG)

You can create custom Security Group that will allow inbound and outbound traffic based on your specification. In this case the Security Group will have inbound traffic as `All traffic` referencing to itself. For outbound taffic specify `All traffic` with destination `0.0.0.0/0`.
![Image 4.14](../media/image_4.14.PNG)

#### MWAA - Managed Workflows for Apache Airflow
Access `Airflow` and press on `Create environment`.
Enter `driven_data_airflow_environment` as *Name* in *Environment details* section. Choose latest version available for Airflow. As our pipeline should be available with fresh data daily at 08:00 AM, choose for `Weekly maintenance window start` after this time and prefered in weekend.
![Image 4.5](../media/image_4.15.PNG)

Press `Browse S3` and choose the bucket that was created before `driven-data-bucket` as *S3 Bucket*. Use same bucket for all options with specific directory inside such as: dags, lib for plugins and requirements. Plugins should be zipped and requirements should be in `txt` format. For this specific environment leave empty all fields beside first one with the bucket itself.
![Image 4.16](../media/image_4.16.PNG)

Choose `Create MWAA VPC` for `Virtual private cloud` option and a VPC will be create special to be used with the MWAA. This option will create as well the private subnets needed for MWAA setup. You can see created private subnets selected as `Subnet 1` and `Subnet 2`.
![Image 4.17](../media/image_4.17.PNG)

Choose `Private network (No internet accessible)` so this Airflow environment will be available only for the users with access to the VPC. Also, choose `Create new security group` to generate a Security Group special for the Airflow environment.
![Image 4.18](../media/image_4.18.PNG)

Choose `Service managed endpoints` for *Endpoint management* option. As an *Environment class* choose `mw1.small`.
![Image 4.19](../media/image_4.19.PNG)

For *Permissions* option choose `Create a new role` as an *Execution role* and choose the name for *Role name* - can be left default name.\
At the end of all these operations, press `Review environment`, review all settings and press `Create environment`.
![Image 4.20](../media/image_4.20.PNG)

After setup the environment you'll se the environment creation process. In this window you can monitor if the creation process will be successful or some errors will occur. If any error occur, check the logs to see the error root cause and redeploy the environment after address the error.
![Image 4.21](../media/image_4.21.PNG)

The environment creation process will take around 30-45 minutes. If all settings were setup correctly we'll see the `Available` status after deployment is finished. Now you can use the MWAA to create the pipeline with the DAG.
![Image 4.22](../media/image_4.22.PNG)

#### IAM - Identity Access Management
Access the IAM section and select `roles` option, here you should see all existing roles. Two roles should be related to the MWAA. First role is the role that was created for the MWAA and it was kept the original name and the second one is a service role for the MWAA.
![Image 4.23](../media/image_4.23.PNG)

Click on the MWAA role and choose the `policy` section. Open the policy and here you'll see what permissions has the role via this policy. For example, the part in the image allow the role to list the buckets name and only for specific bucket with the name `driven-data-bucket`. This policy will be edited in future steps to allow the role to execute necessary operations on specific services.
![Image 4.24](../media/image_4.24.PNG)

