# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-12-20 19:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fatogo_RDB', '0004_auto_20181220_1947'),
    ]

    operations = [
        migrations.AlterField(
            model_name='companyinfomations',
            name='hotelTraffic',
            field=models.IntegerField(default=0),
        ),
    ]
