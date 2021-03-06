# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-12-29 20:28
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AuxiliaryfacilitiesReserveTime',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reservatedDate', models.DateField(blank=True, null=True)),
                ('t00', models.BooleanField(default=False)),
                ('t01', models.BooleanField(default=False)),
                ('t02', models.BooleanField(default=False)),
                ('t03', models.BooleanField(default=False)),
                ('t04', models.BooleanField(default=False)),
                ('t05', models.BooleanField(default=False)),
                ('t06', models.BooleanField(default=False)),
                ('t07', models.BooleanField(default=False)),
                ('t08', models.BooleanField(default=False)),
                ('t09', models.BooleanField(default=False)),
                ('t10', models.BooleanField(default=False)),
                ('t11', models.BooleanField(default=False)),
                ('t12', models.BooleanField(default=False)),
                ('t13', models.BooleanField(default=False)),
                ('t14', models.BooleanField(default=False)),
                ('t15', models.BooleanField(default=False)),
                ('t16', models.BooleanField(default=False)),
                ('t17', models.BooleanField(default=False)),
                ('t18', models.BooleanField(default=False)),
                ('t19', models.BooleanField(default=False)),
                ('t20', models.BooleanField(default=False)),
                ('t21', models.BooleanField(default=False)),
                ('t22', models.BooleanField(default=False)),
                ('t23', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='CompanyAccounts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tid', models.CharField(default='testasdas', max_length=100)),
                ('password', models.CharField(default='testasdas', max_length=100)),
                ('authority', models.CharField(default='testasdas', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='CompanyAddress',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address1', models.CharField(default='testasdas', max_length=100)),
                ('address2', models.CharField(blank=True, default='testasdas', max_length=100, null=True)),
                ('address3', models.CharField(blank=True, default='testasdas', max_length=100, null=True)),
                ('address4', models.CharField(blank=True, default='testasdas', max_length=100, null=True)),
                ('address5', models.CharField(blank=True, default='testasdas', max_length=100, null=True)),
                ('address5_1', models.CharField(blank=True, default='testasdas', max_length=100, null=True)),
                ('address6', models.CharField(blank=True, default='testasdas', max_length=100, null=True)),
                ('address6_1', models.CharField(blank=True, default='testasdas', max_length=100, null=True)),
                ('address7', models.CharField(blank=True, default='testasdas', max_length=100, null=True)),
                ('address8', models.CharField(blank=True, default='testasdas', max_length=100, null=True)),
                ('addressLatitude', models.CharField(default='testasdas', max_length=100)),
                ('addressLongitude', models.CharField(default='testasdas', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='CompanyAroundEnvironment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('EnvironmentName', models.CharField(default='testasdas', max_length=100)),
                ('EnvironmentExplain', models.TextField(default='testasdas', max_length=20000)),
                ('timeForWalk', models.PositiveSmallIntegerField()),
                ('timeForCar', models.PositiveSmallIntegerField()),
                ('serviceStart', models.PositiveSmallIntegerField()),
                ('serviceEnd', models.PositiveSmallIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='CompanyAroundfacilities',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('facilitiesName', models.CharField(default='testasdas', max_length=100)),
                ('facilitiesExplain', models.TextField(default='testasdas', max_length=20000)),
                ('timeForWalk', models.PositiveSmallIntegerField()),
                ('timeForCar', models.PositiveSmallIntegerField()),
                ('serviceStart', models.PositiveSmallIntegerField()),
                ('serviceEnd', models.PositiveSmallIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='CompanyAuxiliaryfacilities',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('facilitiesName', models.CharField(default='testasdas', max_length=100)),
                ('facilitiesNumber', models.PositiveSmallIntegerField()),
                ('onefacilitiesMemberMaxNum', models.PositiveSmallIntegerField()),
                ('onefacilitiesMinTimeCell', models.PositiveSmallIntegerField()),
                ('priceForOneTimeCell', models.IntegerField()),
                ('serviceStart', models.PositiveSmallIntegerField()),
                ('serviceEnd', models.PositiveSmallIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='CompanyInfomations',
            fields=[
                ('identifyCode', models.CharField(max_length=100, primary_key=True, serialize=False, unique=True)),
                ('hotelName', models.CharField(default='testasdas', max_length=100)),
                ('hotelAvgScore', models.CharField(default='testasdas', max_length=3)),
                ('hotelTotalReview', models.PositiveSmallIntegerField(default=0)),
                ('hotelTraffic', models.IntegerField(default=0)),
                ('hotelCheckout', models.IntegerField(default=0)),
                ('hotelCheckin', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='CompanyInnerRoomfacilities',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('facilitiesName', models.CharField(default='testasdas', max_length=100)),
                ('onefacilitiesMemberMaxNum', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='CompanyMasterInfomations',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('masterName', models.CharField(default='testasdas', max_length=100)),
                ('masterRegistrationNumber', models.CharField(default='testasdas', max_length=100)),
                ('masterBusinessLicenseNumber', models.CharField(default='testasdas', max_length=100)),
                ('masterPhoneNumber', models.CharField(default='testasdas', max_length=100)),
                ('masterEmail', models.CharField(default='testasdas', max_length=100)),
                ('companyInfo_CompanyMasterInfomationsFK', models.ForeignKey(default='none', on_delete=django.db.models.deletion.CASCADE, to='fatogo_RDB.CompanyInfomations')),
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
                ('avgScore', models.CharField(default='testasdas', max_length=3)),
                ('reviewedDate', models.DateTimeField(default=django.utils.timezone.now)),
                ('reviewedText', models.TextField(default='testasdas', max_length=2000)),
                ('reviewedGroup', models.CharField(default='testasdas', max_length=100)),
                ('companyInfo_ReviewFK', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fatogo_RDB.CompanyInfomations')),
            ],
        ),
        migrations.CreateModel(
            name='CompanyRoomTypeInfomations',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('roomType', models.CharField(default='testasdas', max_length=100)),
                ('roomWidth', models.PositiveSmallIntegerField(default=0)),
                ('roomHeight', models.PositiveSmallIntegerField(default=0)),
                ('roomsize', models.PositiveSmallIntegerField(default=0)),
                ('roomPrice', models.IntegerField(default=0)),
                ('roomMaxHumanNum', models.IntegerField(default=3)),
                ('roomAvgHumanNum', models.IntegerField(default=1)),
                ('companyInfo_RoomTypeInfomationsFK', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fatogo_RDB.CompanyInfomations')),
            ],
        ),
        migrations.CreateModel(
            name='RoomInfomation',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('roomNum', models.PositiveSmallIntegerField(default=0)),
                ('roomFloor', models.PositiveSmallIntegerField(default=0)),
                ('startPointX', models.PositiveSmallIntegerField(default=0)),
                ('startPointY', models.PositiveSmallIntegerField(default=0)),
                ('companyRoomTypeInfomations_RoomInfomationFK', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fatogo_RDB.CompanyRoomTypeInfomations')),
            ],
        ),
        migrations.CreateModel(
            name='RoomState',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reservationBlock', models.BooleanField(default=False)),
                ('reservated', models.BooleanField(default=False)),
                ('reservatedDate', models.DateField(blank=True, null=True)),
                ('reservationFirstDate', models.DateField(blank=True, null=True)),
                ('reservationEndDate', models.DateField(blank=True, null=True)),
                ('checkoutTime', models.DateTimeField(blank=True, null=True)),
                ('checkinTime', models.DateTimeField(blank=True, null=True)),
                ('roomReservation_roomStateFK', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fatogo_RDB.RoomInfomation')),
            ],
        ),
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('kakaoTalkID', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('tripPerpose', models.CharField(default='testasdas', max_length=100)),
                ('organizationName', models.CharField(default='testasdas', max_length=100)),
                ('startingAreaSI', models.CharField(default='testasdas', max_length=100)),
                ('startingAreaGUUN', models.CharField(default='testasdas', max_length=100)),
                ('startingAreaGU', models.CharField(default='testasdas', max_length=100)),
                ('desiredTripAreaSI', models.CharField(default='testasdas', max_length=100)),
                ('desiredTripAreaGUUN', models.CharField(default='testasdas', max_length=100)),
                ('desiredTripAreaGU', models.CharField(default='testasdas', max_length=100)),
                ('expectMemberNumber', models.PositiveSmallIntegerField()),
                ('desiredAuxiliaryfacilities', models.CharField(max_length=100)),
                ('desiredInnerfacilities', models.CharField(max_length=100)),
                ('desiredAroundfacilities', models.CharField(max_length=100)),
                ('desiredAroundEnvironment', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='roominfomation',
            name='userInfo_RoomReservationFK',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='fatogo_RDB.UserInfo'),
        ),
        migrations.AddField(
            model_name='companyinnerroomfacilities',
            name='companyRoomTypeInfomations_companyInnerRoomfacilitiesFK',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fatogo_RDB.CompanyRoomTypeInfomations'),
        ),
        migrations.AddField(
            model_name='companyauxiliaryfacilities',
            name='companyInfo_AuxiliaryfacilitiesFK',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fatogo_RDB.CompanyInfomations'),
        ),
        migrations.AddField(
            model_name='companyaroundfacilities',
            name='companyInfo_AroundfacilitiesFK',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fatogo_RDB.CompanyInfomations'),
        ),
        migrations.AddField(
            model_name='companyaroundenvironment',
            name='companyInfo_AroundEnvironmentFK',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fatogo_RDB.CompanyInfomations'),
        ),
        migrations.AddField(
            model_name='companyaddress',
            name='companyInfo_AddressFK',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fatogo_RDB.CompanyInfomations'),
        ),
        migrations.AddField(
            model_name='companyaccounts',
            name='companyInfo_AccountsFK',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fatogo_RDB.CompanyInfomations'),
        ),
        migrations.AddField(
            model_name='auxiliaryfacilitiesreservetime',
            name='AuxiliaryfacilitiesFK',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fatogo_RDB.CompanyAuxiliaryfacilities'),
        ),
    ]
