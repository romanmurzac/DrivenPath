# DrivenPath

## Description
**DrivenPath** is a Data Engineering Retraining Program repository. It is designed to guide junior engineers and professionals transitioning into the field of Data Engineering. Through a combination of theoretical knowledge and hands-on practice, anybody can learn how to build, deploy, and manage data pipelines, ultimately creating a comprehensive project applicable to a real-world scenario.\
In this program, any user can learn theoretical and practical aspects to become a proficient Data Engineer by building a complete data pipeline for a simulate small business. The scenario-driven approach ensures that users not only learn the technical skills but also understand how to apply them in a practical context.

## Content
- [Description](#description)
- [Repository Structure](#repository-structure)
- [Getting Started](#getting-started)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

`Work in progress...`

## Repository Structure
DrivenPath is devided in **chapters**.\
If you want to get from zero and at the final to be able to get a Professional Certification or a Junior Big Data Engineer role, follow all the chapters in established order.\
If you want just refresh the knowledge of specific area, go stright forward to that chapter.

### Chapters
Each chapter is focusing on one specific topic and contain theoretical and practical parts.

```
chapter_1
├───src_1
|   |───src_1.md
├───work_1
|   |───delete_me_1.md
└───README.md
```

#### General
The whole repository is built around a real-world scenario. Each chapter start with a specific part from this scenario and further provide theoretical notions to understand how to implement this part. Also, almost all chapters contain practical part of implementation to fulfill this part.  

#### Chapter 1: Scenario
*Introduction to Big Data Engineering* chapter contain notions about the Big Data field.

#### Chaper 2: Big Data Engineering
*Batch processing - Local Development* chapter contain notions about Batch processing and practical part for ETL pipeline creation based on scenario requirements.


`Work in progress...`

## Getting Started
1. Login to GitHub.\
Navigate to [GitHub](https://github.com/) and `Sign in` using your credentials or create new account using `Sign up` if don't have one and follow instructions from *Chapter 1*.

2. Navigate to DrivenPath.\
Navigate to [DrivenPath](https://github.com/romanmurzac/DrivenPath) repository.

3. Fork DrivenPath.\
Once you're in DrivenPath repository main page, click on `Fork` option as in image below and proceed to the next page.
![Fork DrivenPath.](media/image_0.1.PNG "Fork DrivenPath")

4. Complete Fork.\
Complete fork information in order to obtain a copy of the original repository. This copy of repository will be your personal space to go through the whole learning process.
![Complete Fork process.](media/image_0.2.PNG "Complete Fork process")

5. Clone Your DrivenPath.\
On your local computer open a terminal and choose where you want to store the *DrivenPath* project, in command below replace `repository-path` with your actual path. Also, replace `your-username` with your GitHub username.
```
cd <repository-path>
git clone https://github.com/<your-username>/DrivenPath.git
```

6. Create Branch.\
There recomendation is to create a separate branch for each chapter. In terminal introduce the command below by replacing the `no` with the chapter number.
```
git checkout -b chapter_<no>
```
On each step that you perform commit your changes and push them at the end of working period.
```
git add .
git commit -m "Chapter <no>: Update SQL for create_pii_data.sql file."
git push
```

## Contributing
Contributions are welcome! If you find any issues or want to enhance the program, feel free to fork / clone the repository and submit a pull request.

## License
This project is licensed under the MIT License - see the LICENSE file for details.

## Contact
If you have any questions or need support, please open an issue in the repository or reach out via [LinkedIn](https://www.linkedin.com/in/roman-murzac/) message.
