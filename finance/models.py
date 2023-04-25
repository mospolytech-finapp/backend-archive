from django.db import models
import datetime


class Transaction(models.Model):
    name = models.CharField(max_length=128, blank=True, null=True)
    user_id = models.ForeignKey('authentication.Finapp_User', on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=12, decimal_places=2, blank=False, null=False)
    date = models.DateField(blank=False, null=False, default=datetime.date.today)
    time = models.TimeField(blank=True, null=True)
    description = models.CharField(max_length=128, blank=True, null=True)
    category = models.ForeignKey('finance.Category', on_delete=models.DO_NOTHING, blank=False, null=False)


class Category(models.Model):
    name = models.CharField(max_length=255)
