FROM python:3.7-alpine

ENV PYTHONUNBUFFERED 1

RUN python -m pip install --upgrade pip

COPY requirements.txt requirements.txt
RUN python -m pip install -r requirements.txt

RUN mkdir /proj_prob
WORKDIR /proj_prob

COPY ./proj_prob /proj_prob