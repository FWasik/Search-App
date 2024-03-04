# Search App

## Table of contents
* [General info](#general-info)
* [Technologies](#technologies)
* [Setup](#setup)
* [CI/CD with GitHub Actions and AWS Elastic Beanstalk](#cicd-with-github-actions-and-aws-elastic-beanstalk)


## General info
The purpose of the application is to search for medical articles from sites such as PubMed, Lancet, and NEJM. 
For this purpose web scraping was used. To create the website tools like Django, BeatifulSoup, docker-compose were used. 
CI/CD pipeline was set up with GitHub Actions and production environment on AWS Elastic Beanstalk. The app is deployed 
here: http://search-app.eu-central-1.elasticbeanstalk.com/


## Technologies
* Python: 3.9.2
* Django: 4.0.3
* BeautifulSoup4: 4.10.0
* Docker, docker-compose
* GitHub Actions
* AWS Elastic Beanstalk


## Setup
To run an app on your computer you can pull docker image from my DockerHub account with this command:
```
docker pull dilreni2137/search-app:dev
```

Then you must run container:
```
docker run -p 8000:8000 -t dilreni2137/search-app:dev
```

Now an app should be running at http://127.0.0.1:8000/ and http://localhost:8000/ 


## CI/CD with GitHub Actions and AWS Elastic Beanstalk
Due to creation of a full CI/CD pipeline (except testing stage - no tests in this project), GitHub Actions and AWS EBS 
were used. Each push to main branch triggers a workflow which builds two types of images: development and production. 
Then, both of them are push to DockerHub. After that, production job starts. It pulls a production 
image from DockerHub, zips it and sends to AWS EBS service. Eventually, EBS deploys it in a given environment.


