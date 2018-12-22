# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-12-20 11:15
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('fatogo_RDB', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CompanyAroundEnvironment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('EnvironmentName', models.CharField(max_length=100)),
                ('EnvironmentExplain', models.TextField(max_length=100000)),
                ('timeForWalk', models.PositiveSmallIntegerField()),
                ('timeForCar', models.PositiveSmallIntegerField()),
                ('serviceStart', models.PositiveSmallIntegerField()),
                ('serviceEnd', models.PositiveSmallIntegerField()),
                ('companyInfo_AroundEnvironmentFK', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fatogo_RDB.CompanyInfomations')),
            ],
        ),
        migrations.CreateModel(
            name='CompanyReview',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comfortableScore', models.PositiveSmallIntegerField()),
                ('cleanessScore', models.PositiveSmallIntegerField()),
                ('auxiliaryFacilityScore', models.PositiveSmallIntegerField()),
                ('newerScore', models.PositiveSmallIntegerField()),
                ('companyInfo_AroundEnvironmentFK', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fatogo_RDB.CompanyInfomations')),
            ],
        ),
        migrations.RemoveField(
            model_name='companayaroundenvironment',
            name='companyInfo_AroundEnvironmentFK',
        ),
        migrations.DeleteModel(
            name='CompanayAroundEnvironment',
        ),
    ]