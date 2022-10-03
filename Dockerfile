# The first instruction is what image we want to base our container on
# We Use an official Python runtime as a parent image
FROM python:3.10.5

# setup environment variable
ENV DockerHOME=be-challenge/

# set work directory
RUN mkdir -p /be-challenge

# where your code lives
WORKDIR /be-challenge

ADD . /be-challenge

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
RUN pip install --upgrade pip


# run this command to install all dependencies
RUN pip install -r requirements.txt
# port where the Django app runs
EXPOSE 8000
# start server
CMD python manage.py migrate

CMD python manage.py runserver '127.0.0.1:8000'