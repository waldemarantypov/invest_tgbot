FROM postgres:9.5.23
ADD ./db.sql /docker-entrypoint-initdb.d/

FROM python:3.8

ENV PYTHONUNBUFFERED=1

RUN mkdir /code
WORKDIR /code

COPY requirements.txt /code/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . /code/