FROM python:3

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
RUN apt-get update && apt-get install -y gettext

COPY . .

RUN ["python", "./manage.py", "makemigrations"]
RUN ["python", "./manage.py", "migrate"]
RUN ["python", "./manage.py", "compilemessages"]

ENTRYPOINT [ "gunicorn", "-b", "0.0.0.0:8000", "backend.wsgi" ]
