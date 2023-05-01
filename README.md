# backend

## Ручной запуск

> Linux, Unix

```
docker-compose up -d --build
docker-compose exec web python manage.py compilemessages
docker-compose exec web python manage.py migrate --noinput
```

## Просмотр бд

```
docker-compose exec db psql --username=fintool_dev --dbname=fintool
```
