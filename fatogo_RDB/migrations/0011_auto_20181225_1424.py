# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-12-25 14:24
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fatogo_RDB', '0010_companyinfomations_hoteltotalreivew'),
    ]

    operations = [
        migrations.RenameField(
            model_name='companyinfomations',
            old_name='hotelTotalReivew',
            new_name='hotelTotalReview',
        ),
    ]
