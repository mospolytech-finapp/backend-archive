from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from .managers import FinappUserManager


class Finapp_User(AbstractBaseUser):
    last_name = models.CharField(
        'Фамилия', max_length=30, null=False, blank=False)
    first_name = models.CharField(
        'Имя', max_length=30, null=False, blank=False)
    middle_name = models.CharField(
        'Отчество', max_length=30, null=True, blank=True)
    email = models.EmailField(
        unique=True, null=False, blank=False)
    date_of_birth = models.DateField(
        'Дата рождения', null=True, blank=True)

    USERNAME_FIELD = 'email'

    objects = FinappUserManager()

    def __str__(self):
        return f"{self.last_name} {self.first_name} {self.middle_name}"

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
