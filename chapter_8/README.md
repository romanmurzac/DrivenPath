# **Chapter 8:** Streaming processing - *Cloud Pipeline*

**NOTE:** This chapter involve work with cloud services that are charged by the cloud provider. Consult [AWS Pricing calculator](https://calculator.aws/#/) for forecast of the estimated cost of the services used for current chapter.\
If you proceed with this chapter this is on your own responsability and the author don't have any responsability for the resulted bill.

## Scenario
For ninth Chapter / Sprint, as the *DrivenData* company exptect a big amount of data daily and also increasing requests from other departments for different analytics, it is required to process on daily basis data from previous two days from datalake that is stored in S3 bucket and process data by filtering and aggregating and also add aditional columns based on existing ones. After transformations it is required to write data back to the datalake. Check if there are missing values for emails and phone numbers; provide correct datatypes for birth dates and sessions duration; delete duplicated records; provide only the records that are from 2024 and have a session duration was longer than 30 minutes; add column for total consumed bandwith; add a column for activity level of the user; add a column with masked emails; provide data for filtered data for and for grouped data.

## Assignment
For current Sprint / Chapter your tasks are:
1. **Read** from [Theory](#theory) section about:\
    a. Lambda Function.\
    b. Simple Queue Service.\
    c. JSON.

2. **Implement** from [Practice](#practice) section for *DataDriven* company:\
    a. Create IAM role.

    b. Setup Simple Queue Service:
    * i. Create Simple Queue Service.
    * ii. Test Simple Queue Service.

    c. Setup producer Lambda function:
    * i. Create producer Lambda function.
    * ii. Test producer Lambda function.
    * iii. Run producer Lambda.

    d. Setup consumer Lambda function:
    * i. Create consumer Lambda function.
    * ii. Test consumer Lambda function.
    * iii. Run consumer Lambda.

3. **Work** for *LeadData* company on Sprint / Chapter tasks:\
Read chapter *Scenario*, implement all stages from *Assignment* from `work_9/scenario_9.md` file and put all your work evidences in `work_9` directory.

## Theory
Main theoretical notions of the chapter with proper resources for self paced learning.

### Lambda Function
#### Description
#### References
[]()\
[]()\
[]()

### Simple Queue Service
#### Description
#### References
[]()\
[]()\
[]()

### JSON
#### Description
#### References
[]()\
[]()\
[]()

## Practice
Implemention for the practical part of the chapter.
