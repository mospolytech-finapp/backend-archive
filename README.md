# backend

## Ручной запуск

> Linux, Unix

### Продакшн

```
sudo ./init-letsencrypt.sh
docker-compose -f docker-compose.prod.yml up -d --build
docker-compose -f docker-compose.prod.yml exec web python manage.py compilemessages
docker-compose -f docker-compose.prod.yml exec web python manage.py migrate --noinput
```

### Разработка

```
docker-compose up -d --build
docker-compose exec web python manage.py compilemessages
docker-compose exec web python manage.py migrate --noinput
```

## Просмотр бд

```
docker-compose exec db psql --username=fintool_dev --dbname=fintool
```
