FROM python:3.13-alpine

COPY . /workout-api

WORKDIR /workout-api

RUN pip install -r requirements.txt