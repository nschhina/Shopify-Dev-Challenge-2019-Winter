FROM python:3.6

ENV PYTHONUNBUFFERED 1

# create root directory for our project in the container
RUN mkdir /shopify

COPY requirements.txt /shopify

WORKDIR /shopify

ADD api /shopify/

RUN pip install -r requirements.txt

RUN python manage.py runserver
