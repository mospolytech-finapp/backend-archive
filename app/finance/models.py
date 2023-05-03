from django.db import models
from django.conf import settings
from django.db.models import Sum
import datetime


# Транзакции
class Transaction(models.Model):
    name = models.CharField(
        max_length=128, blank=True, null=True)
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    amount = models.DecimalField(
        max_digits=12, decimal_places=2, blank=False, null=False)
    date = models.DateField(
        blank=False, null=False, default=datetime.date.today)
    time = models.TimeField(
        blank=True, null=True)
    description = models.CharField(
        max_length=128, blank=True, null=True)
    category = models.ForeignKey(
        'finance.Category', on_delete=models.DO_NOTHING, blank=False, null=False)


class Category(models.Model):
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)


# Цели
class Goal(models.Model):
    name = models.CharField(
        max_length=128, blank=False, null=False)
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    opening_date = models.DateField(
        blank=False, null=False, default=datetime.date.today)
    achievement_date = models.DateField(
        blank=False, null=False)
    amount_target = models.DecimalField(
        max_digits=12, decimal_places=2, blank=False, null=False)

    def get_amount_now(self):
        return sum(goal_transaction.amount for goal_transaction in self.goal_transaction_set.all())


class Goal_Transaction(models.Model):
    goal = models.ForeignKey(
        Goal, on_delete=models.CASCADE)
    amount = models.DecimalField(
        max_digits=12, decimal_places=2, blank=False, null=False)
    date = models.DateField(
        blank=False, null=False)
    description = models.CharField(
        max_length=128, blank=True, null=True)
