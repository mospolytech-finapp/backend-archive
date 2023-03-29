import uuid
from django.db import models

# Create your models here.

class Transaction(models.Model):

    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4)
    user_uuid = models.ForeignKey(
        'authentication.CustomUser',
        on_delete=models.CASCADE,
    )
    name = models.CharField(max_length=128, blank=True)
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    type = models.BooleanField() #false - Расход / true - Поступление
    date_time = models.DateTimeField(auto_now_add=True)
    description = models.CharField(max_length=128, blank=True)

    #def create_transaction(self, user_uuid, amount, type, **extra_fields):
    #    tr = self.model(user_uuid=user_uuid, amount=amount, type=type, **extra_fields)
    #    tr.save()

    #    return tr

    def __str__(self):
        return self.type


class CategoryLink(models.Model):
    tr_uuid = models.ForeignKey(
        'Transaction',
        on_delete=models.CASCADE,
    )
    category_uuid = models.ForeignKey(
        'Category',
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.type


class Category(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4)
    name = models.CharField(max_length=15)

    def __str__(self):
        return self.type


class TagLink(models.Model):
    tr_uuid = models.ForeignKey(
        'Transaction',
        on_delete=models.CASCADE,
    )
    tag_uuid = models.ForeignKey(
        'Tag',
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.type


class Tag(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4)
    name = models.CharField(max_length=15)

    def __str__(self):
        return self.type
