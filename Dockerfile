FROM python:3.6

ENV PYTHONUNBUFFERED 1

# create root directory for our project in the container
RUN mkdir /shopify

COPY requirements.txt /shopify

ADD api /shopify/

WORKDIR /shopify

RUN pip install -r requirements.txt

EXPOSE 8000

CMD python /shopify/manage.py runserver 0.0.0.0:8000
