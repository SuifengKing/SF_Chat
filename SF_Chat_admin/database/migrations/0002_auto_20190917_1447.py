# Generated by Django 2.1.5 on 2019-09-17 06:47

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usersprofile',
            name='date_joined',
            field=models.DateTimeField(default=datetime.datetime.now, verbose_name='注册时间'),
        ),
    ]
