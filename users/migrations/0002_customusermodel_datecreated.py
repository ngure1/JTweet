# Generated by Django 5.0.1 on 2024-02-05 15:16

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customusermodel',
            name='dateCreated',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]