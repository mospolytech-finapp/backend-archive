# Generated by Django 4.1.7 on 2023-03-31 13:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=128)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=12)),
                ('type', models.BooleanField()),
                ('date_time', models.DateTimeField(auto_now_add=True)),
                ('description', models.CharField(blank=True, max_length=128)),
                ('user_uuid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='TagLink',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag_uuid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='finance.tag')),
                ('tr_uuid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='finance.transaction')),
            ],
        ),
        migrations.CreateModel(
            name='CategoryLink',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_uuid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='finance.category')),
                ('tr_uuid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='finance.transaction')),
            ],
        ),
    ]
