# Search App

## Table of contents
* [General info](#general-info)
* [Technologies](#technologies)
* [Setup](#setup)


## General info
The purpose of the application is to search for medical articles from sites such as PubMed, Lancet, and NEJM. 
For this purpose web scraping was used. To create the website tools like Django, BeatifulSoup, docker-compose were used. 
A workflow was set up with GitHub Actions to publish images to DockerHub.


## Technologies
* Python: 3.9.2
* Django: 4.0.3
* BeautifulSoup4: 4.10.0
* Docker, docker-compose
* GitHub Actions

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


