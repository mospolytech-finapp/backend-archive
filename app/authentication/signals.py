from django.db.models.signals import post_save
from django.dispatch import receiver
from finance.models import Category

from django.contrib.auth import get_user_model
User = get_user_model()

DEFAULT_CATEGORIES = [
    'Работа',
    'Подработка',
    'Пособие',
    'Премия',
    'Транспорт',
    'ЖКХ',
    'Продукты',
    'Еда',
    'Развлечения',
    'Образование',
    'Подарки',
    'Налоги',
    'Семья/дети',
    'Путешествия',
    'Вредные привычки',
    'Здоровье',
    'Подписки',
    'Одежда',
    'Животные',
    'Прочее',
]


@receiver(post_save, sender=User)
def create_default_categories(sender, instance, created, **kwargs):
    if created:
        for category_name in DEFAULT_CATEGORIES:
            Category.objects.create(owner=instance, name=category_name)
