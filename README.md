# Search App

## Table of contents
* [General info](#general-info)
* [Technologies](#technologies)
* [Setup](#setup)

## General info
The purpose of the application is to search for medical articles from sites such as PubMed, Lancet, and NEJM. 
For this purpose web scraping was used. To create the website tools like Django, BeatifulSoup, docker-compose were used. 
The application was deployed using the Heroku platform.

You can use app here:   
https://search-med-app.herokuapp.com/

## Technologies
* Python: 3.9.2
* Django: 4.0.3
* BeautifulSoup4: 4.10.0
* Docker, docker-compose
* Heroku platform


## Setup
Sites which are helpful before installation of requirements:    
https://www.python.org/downloads/  
https://www.docker.com/

Before installing requirements, create virtual environment.

Virtual environment configuration:  
https://docs.python-guide.org/dev/virtualenvs/

Requirements must be install. Install from requirements.txt:
```
pip install -r requirements.txt 
```

Install from Pipfile (with pipenv):
```
pipenv install
```


## Run

#### Without Docker:
```
py manage.py runserver
```

#### With Docker:
```
docker-compose build

docker-compose up -d
```

#### Inspecting container:
```
docker-compose logs -f
```


#### Running production version:
```
docker-compose -f docker-compose.prod.yml up -d --build  
```


