FROM python:3.13-alpine

COPY . /workoutapi

WORKDIR /workoutapi

RUN pip install -r requirements.txt