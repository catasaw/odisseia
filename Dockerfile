FROM python:2.7

ADD requirements.txt /app/requirements.txt

RUN apt-get update

RUN pip install -r /app/requirements.txt

EXPOSE 8000

