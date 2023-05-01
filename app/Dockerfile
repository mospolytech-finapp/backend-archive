FROM python:alpine

WORKDIR /usr/src/app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
RUN apk --no-cache add gettext

COPY . .

RUN ["python", "./manage.py", "migrate"]
RUN ["python", "./manage.py", "compilemessages"]

ENTRYPOINT [ "gunicorn", "-b", "0.0.0.0:8000", "backend.wsgi" ]
