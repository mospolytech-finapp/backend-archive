from django.db import models


class Transactions(models.Model):
    name = models.CharField(max_length=128, blank=True, null=True)
    user_id = models.ForeignKey('authentication.Finapp_User', on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=12, decimal_places=2, blank=False, null=False)
    is_arrival = models.BooleanField(blank=False, null=False)  # false - Расход / true - Поступление
    date = models.DateField(auto_now_add=True, blank=False, null=False)
    time = models.TimeField(blank=True, null=True)
    description = models.CharField(max_length=128, blank=True, null=True)
    # category = models.ForeignKey('finance.Category', blank=False, null=False, on_delete=models.DO_NOTHING)
    category = models.IntegerField(blank=False, null=False)


class Category(models.Model):
    name = models.CharField(max_length=255)
