# be-challenge
Backend challenge Python for Santex Group

# Model structure optimizations:
## TeamMember

Instead of creating two models to store players and coach, an Model called
TeamMember was created. The reason is that what differs a tem member from another is their role,
so a field  called "role" was created to store the 

#  Database:
Since its a small project, with no large amount of data, 
just as was deployed on a free hosting platform, SQLite3 was choose to handle our data. 

#  Third party libraries:

### django-filter (https://django-filter.readthedocs.io/):
Used to make it easier to filter in viewsets

### drf-spetacular (https://drf-spectacular.readthedocs.io/):
OpenAPI 3.0 schema generation for the API.


# Running te API:
There are 3 ways to run this project.

### 1 - Access: http://josiano.pythonanywhere.com


### 2 - Via Docker:
With docker installed, just access the project directory an type: 


### 3 - Run in your machine. 


# Unit tests:

Setup your environment (step 3 above) and the type `python manage.py test`
