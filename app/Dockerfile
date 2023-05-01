FROM python:alpine

WORKDIR /usr/src/app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
RUN apk update
RUN apk --no-cache add \
  postgresql-dev gcc python3-dev musl-dev
RUN apk --no-cache add gettext

COPY . .
