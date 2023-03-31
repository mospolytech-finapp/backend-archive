import uuid
from django.db import models


class Transaction(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4)
    name = models.CharField(max_length=128, blank=True)
    #user_uuid = models.ForeignKey('authentication.CustomUser', on_delete=models.CASCADE,)
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    type = models.BooleanField()  # false - Расход / true - Поступление
    date_time = models.DateTimeField(auto_now_add=True)
    description = models.CharField(max_length=128, blank=True)


class CategoryLink(models.Model):
    tr_uuid = models.ForeignKey(
        'Transaction',
        on_delete=models.CASCADE,
    )
    category_uuid = models.ForeignKey(
        'Category',
        on_delete=models.CASCADE,
    )


class Category(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4)
    name = models.CharField(max_length=15)


class TagLink(models.Model):
    tr_uuid = models.ForeignKey(
        'Transaction',
        on_delete=models.CASCADE,
    )
    tag_uuid = models.ForeignKey(
        'Tag',
        on_delete=models.CASCADE,
    )


class Tag(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4)
    name = models.CharField(max_length=15)
