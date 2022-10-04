# Backend challenge Python for Santex Group

Python version: 3.10+

# Model structure optimizations:
## TeamMember

Instead of creating two models to store players and coach, a Model called
TeamMember was created. The reason is that what differs a tem member from another is their role,
so a field  called "role" was created to determine if it's either a coach or player. 

#  Database:
Since it's a small project, with no large amount of data, 
just as was deployed on a free and limited hosting platform (pythonanywhere.com), SQLite3 was chosen to handle our data.

.env database config allows to use another database configuration.

#  Third party libraries:

### django-filter (https://django-filter.readthedocs.io/):
Used to make it easier to filter in viewsets.

### drf-spetacular (https://drf-spectacular.readthedocs.io/):
OpenAPI 3.0 schema generation for the API.


# Running the API:
There are 3 ways to run this project.

### 1 - Access: http://josiano.pythonanywhere.com


### 2 - Via Docker:
With docker installed in your OS, access the project root and run:

`docker build . -t be_challenge`

`docker run be_challenge`


### 3 - Run in your machine. 

Create VirtualEnv with python 3.10+ 

Install requirements: `pip install -r requirements.txt `

Create your .env file.

Here are the .env variables used for the project:

`DATABASE_URL=sqlite://./db.sqlite3`

`FOOTBALL_DATA_API_TOKEN='063796335a0e4a71af30ea480138011a' `

You can use another database and your own football data api token.

Aply migrations: `python manage.py migrate`

Run: `python manage.py runserver`


# Unit tests:

Set up your environment (option 3 in the list above) and then type `python manage.py test`
