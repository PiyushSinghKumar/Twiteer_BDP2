# Twitter Sentiment Analysis
## Overview

This project is a data-driven application that aims to extract data from twitter using api, clean and transform it, store it in a cloud, and then train and deploy a deep learning model to predict certain outcomes. The process involves creating a cluster in AWS and deploying the docker container as a service.


## Tools and Technologies Used

-	Programming Languages: Python
-	Data Extraction: Twitter API
-	Database: S3 bucket
-	Data Version Control: DVC
-	ETL Pipeline: Python
-	Deep Learning Framework: TensorFlow
-	Deployment: Docker
-	CI/CD/CT Pipeline: AWS CodePipeline

## Project Requirements

-	Extract data using Web Scraping or APIs or Streaming Data or Batch Data.
-	Create a Database model and store the extracted data in a database of your choice.
-	Apply Data Version Control (DVC) concept on the database.
-	Create an ETL pipeline with Data Cleaning, Data transformation.
-	Train a Deep Learning model for the application.
-	Deploy the Deep Learning model in the production.
-	Monitor the performance of the ML model.
-	Perform automation of the complete execution of the project.
-	Create a CI/CD/CT pipeline and deploy it.

## Steps to run the project

### Using Docker image:

1.	Pull the Docker image from the ECR registry.

```sh
$ docker pull <ecr-url>/<repository-name>:<tag> 
```

2. Run the Docker container.

```sh
$ docker run -it -p 8000:8000 <ecr-url>/<repository-name>:<tag>
```

3.	The application will now be accessible at:


```sh
http://localhost:5000.
```

### Using AWS external link to the deployed container:

```sh

```

## Conclusion

This project demonstrates the end-to-end implementation of a data-driven application that involves data extraction, cleaning, transformation, and storage in a cloud service provider. It also involves training and deployment of a deep learning model, and monitoring its performance. The project has been implemented using various tools and technologies such as Python, Amazon S3, DVC, TensorFlow, Docker, and Amazon Codepipeline.
