FROM python:3.8

WORKDIR /app/

COPY ./app /app

RUN pip install --upgrade pip

RUN pip install pipenv

RUN pipenv lock

RUN pipenv install --system

ENV PYTHONPATH=/app