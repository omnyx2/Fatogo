# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
# Name of all models
"""
UserInfo
CompanyInfomations
CompanyMasterInfomations
CompanyAccounts
CompanyReview
CompanyAddress
CompanyAuxiliaryfacilities
CompanyAroundfacilities
CompanyInnerRoomfacilities
CompanyAroundEnvironment
"""

# Create your models here.

class UserInfo(models.Model):
    #identifing user
    kakaoTalkID = models.CharField(max_length=100, primary_key=True)
    
    #basic condition
    tripPerpose = models.CharField(max_length=100, default='testasdas')
    organizationName = models.CharField(max_length=100, default='testasdas')
    startingAreaSI = models.CharField(max_length=100, default='testasdas')
    startingAreaGUUN = models.CharField(max_length=100, default='testasdas')
    startingAreaGU = models.CharField(max_length=100, default='testasdas')
    desiredTripAreaSI = models.CharField(max_length=100, default='testasdas')
    desiredTripAreaGUUN = models.CharField(max_length=100, default='testasdas')
    desiredTripAreaGU = models.CharField(max_length=100, default='testasdas')
    expectMemberNumber = models.PositiveSmallIntegerField()
    
    #desired facilities
    desiredAuxiliaryfacilities = models.CharField(max_length=100)
    desiredInnerfacilities = models.CharField(max_length=100)
    desiredAroundfacilities = models.CharField(max_length=100)
    desiredAroundEnvironment = models.CharField(max_length=100)
    
    #reservedroom
    reservedroom = models.CharField
    reservedPrice = models.CharField
    reservedAuxiliaryfacilities = models.CharField
    def __unicode__(self):
        return '%s' % self.kakaoTalkID
    
    
class CompanyInfomations(models.Model):
    identifyCode = models.CharField(max_length=100, primary_key=True, unique=True)
    hotelName = models.CharField(max_length=100, default='testasdas')
    hotelAvgScore = models.CharField(max_length=3, default='testasdas')
    hotelTotalReview = models.PositiveSmallIntegerField(default=0)
    hotelTraffic = models.IntegerField(default=0)
    hotelCheckout = models.IntegerField(default=0)
    hotelCheckin  = models.IntegerField(default=0)
    def __unicode__(self):
        return '%s' % self.identifyCode
    
class CompanyMasterInfomations(models.Model):
    companyInfo_CompanyMasterInfomationsFK = models.ForeignKey('CompanyInfomations', on_delete=models.CASCADE, default='none')
    masterName = models.CharField(max_length=100, default='testasdas')
    masterRegistrationNumber = models.CharField(max_length=100, default='testasdas')
    masterBusinessLicenseNumber = models.CharField(max_length=100, default='testasdas')
    masterPhoneNumber = models.CharField(max_length=100, default='testasdas')
    masterEmail = models.CharField(max_length=100, default='testasdas')
    def __unicode__(self):
        return '%s' % self.companyInfo_CompanyMasterInfomationsFK.identifyCode
    
class CompanyAccounts(models.Model):
    companyInfo_AccountsFK = models.ForeignKey('CompanyInfomations', on_delete=models.CASCADE)
    tid = models.CharField(max_length=100, default='testasdas')
    password = models.CharField(max_length=100, default='testasdas')
    authority = models.CharField(max_length=100, default='testasdas')
    # 0 is Root, 1 is master, 2 is admin, 3 is user
    def __unicode__(self):
        return '%s' % self.companyInfo_AccountsFK.identifyCode
    
class CompanyAddress(models.Model):
    
    companyInfo_AddressFK = models.ForeignKey('CompanyInfomations', on_delete=models.CASCADE)
    
    #광역자치단체 = address1
    #기초자치단체 = address2
    #행정시,일반구 = address3
    #읍,면 = address4
    #도로명(동, 리) = address5, address5_1
    #건물번호(번지) = address6, address6_1
    #상세주소 = address7
    #참고사항 = address8 
    address1 = models.CharField(max_length=100, default='testasdas',)
    address2 = models.CharField(max_length=100, default='testasdas',null=True, blank=True)
    address3 = models.CharField(max_length=100, default='testasdas',null=True, blank=True)
    address4 = models.CharField(max_length=100, default='testasdas',null=True, blank=True)
    address5 = models.CharField(max_length=100, default='testasdas',null=True, blank=True)
    address5_1 = models.CharField(max_length=100, default='testasdas',null=True, blank=True)
    address6 = models.CharField(max_length=100, default='testasdas',null=True, blank=True)
    address6_1 = models.CharField(max_length=100, default='testasdas',null=True, blank=True)
    address7 = models.CharField(max_length=100, default='testasdas',null=True, blank=True)
    address8 = models.CharField(max_length=100, default='testasdas',null=True, blank=True)
    
    #위도 경도 정보
    addressLatitude = models.CharField(max_length=100, default='testasdas')
    addressLongitude = models.CharField(max_length=100, default='testasdas') 
    def __unicode__(self):
        return '%s' % self.companyInfo_AddressFK.identifyCode
    
class CompanyAuxiliaryfacilities(models.Model):
    #PF
    id = models.AutoField(primary_key=True)
    #FK
    companyInfo_AuxiliaryfacilitiesFK = models.ForeignKey('CompanyInfomations', on_delete=models.CASCADE)
    #기본정보
    facilitiesName = models.CharField(max_length=100, default='testasdas')
    facilitiesNumber = models.PositiveSmallIntegerField()
    onefacilitiesMemberMaxNum = models.PositiveSmallIntegerField()
    #단위시간
    onefacilitiesMinTimeCell = models.PositiveSmallIntegerField()
    priceForOneTimeCell = models.IntegerField()
    serviceStart = models.PositiveSmallIntegerField()
    serviceEnd =  models.PositiveSmallIntegerField()
    def __unicode__(self):
        return '%s' % self.companyInfo_AuxiliaryfacilitiesFK.identifyCode+self.facilitiesName

class CompanyAroundfacilities(models.Model):
    companyInfo_AroundfacilitiesFK = models.ForeignKey('CompanyInfomations', on_delete=models.CASCADE)
    #기본정보 시간은 전부 분단위
    facilitiesName = models.CharField(max_length=100, default='testasdas')
    facilitiesExplain = models.TextField(max_length=20000, default='testasdas')
    timeForWalk  = models.PositiveSmallIntegerField()
    timeForCar = models.PositiveSmallIntegerField()
    serviceStart = models.PositiveSmallIntegerField()
    serviceEnd =  models.PositiveSmallIntegerField()
    def __unicode__(self):
        return '%s' % self.companyInfo_AroundfacilitiesFK.identifyCode  
        

class CompanyAroundEnvironment(models.Model):
    companyInfo_AroundEnvironmentFK = models.ForeignKey('CompanyInfomations', on_delete=models.CASCADE)
    
    #기본정보
    EnvironmentName = models.CharField(max_length=100, default='testasdas')
    EnvironmentExplain = models.TextField(max_length=20000, default='testasdas')
    timeForWalk  = models.PositiveSmallIntegerField()
    timeForCar = models.PositiveSmallIntegerField()
    serviceStart = models.PositiveSmallIntegerField()
    serviceEnd =  models.PositiveSmallIntegerField()
    def __unicode__(self):
        return '%s' % self.companyInfo_AroundEnvironmentFK.identifyCode
    
class CompanyRoomTypeInfomations(models.Model):
    
    id = models.AutoField(primary_key=True)
    companyInfo_RoomTypeInfomationsFK = models.ForeignKey('CompanyInfomations', on_delete=models.CASCADE)
    
    roomType = models.CharField(max_length=100, default='testasdas')
    roomWidth = models.PositiveSmallIntegerField(default=0)
    roomHeight = models.PositiveSmallIntegerField(default=0)
    roomsize = models.PositiveSmallIntegerField(default=0)
    roomPrice = models.IntegerField(default=0)
    roomMaxHumanNum = models.IntegerField(default=3)
    roomAvgHumanNum = models.IntegerField(default=1)
    def __unicode__(self):
        return '%s' % self.companyInfo_RoomTypeInfomationsFK+self.roomType
    
class CompanyInnerRoomfacilities(models.Model):
   
    companyRoomTypeInfomations_companyInnerRoomfacilitiesFK = models.ForeignKey('CompanyRoomTypeInfomations', on_delete=models.CASCADE)
    #기본정보
    facilitiesName = models.CharField(max_length=100, default='testasdas')
    onefacilitiesMemberMaxNum = models.IntegerField() 
    def __unicode__(self):
        return '%s' % self.facilitiesName
        
        
class CompanyReview(models.Model):
    
    companyInfo_ReviewFK = models.ForeignKey('CompanyInfomations', on_delete=models.CASCADE)
    #4 types of score
    comfortableScore = models.PositiveSmallIntegerField()
    cleanessScore = models.PositiveSmallIntegerField()
    auxiliaryFacilityScore = models.PositiveSmallIntegerField()
    newerScore = models.PositiveSmallIntegerField()
    avgScore = models.CharField(max_length=3, default='testasdas')
    #Review info
    reviewedDate = models.DateTimeField(default=timezone.now)
    reviewedText = models.TextField(max_length = 2000, default='testasdas')
    reviewedGroup =  models.CharField(max_length=100, default='testasdas')

    def __unicode__(self):
        return '%s' % self.companyInfo_ReviewFK.identifyCode

    
#######################################################    
#Room reservationSystem

class RoomInfomation(models.Model):
    id = models.AutoField(primary_key=True)
    roomNum = models.PositiveSmallIntegerField(default=0)
    roomFloor = models.PositiveSmallIntegerField(default=0)
    
    startPointX = models.PositiveSmallIntegerField(default=0)
    startPointY = models.PositiveSmallIntegerField(default=0)
    #referencing
    userInfo_RoomReservationFK = models.ForeignKey('UserInfo', null=True, blank=True)
    companyRoomTypeInfomations_RoomInfomationFK =models.ForeignKey(CompanyRoomTypeInfomations)
    def __unicode__(self):
        return '%d' % (self.roomNum)

    
    
class RoomState(models.Model):
    roomReservation_roomStateFK = models.ForeignKey(RoomInfomation)
    reservationBlock = models.BooleanField(default=False)
    reservated = models.BooleanField(default=False)                                         
    reservatedDate = models.DateField(blank=True, null=True)
    reservationFirstDate = models.DateField(blank=True, null=True)
    reservationEndDate = models.DateField(blank=True, null=True)
    checkoutTime = models.DateTimeField(blank=True, null=True)
    checkinTime = models.DateTimeField(blank=True, null=True)
    
class AuxiliaryfacilitiesReserveTime(models.Model):
    AuxiliaryfacilitiesFK = models.ForeignKey('CompanyAuxiliaryfacilities', on_delete=models.CASCADE)
    reservatedDate = models.DateField(blank=True, null=True)
    t00 = models.BooleanField(default=False)
    t01 = models.BooleanField(default=False)
    t02 = models.BooleanField(default=False)
    t03 = models.BooleanField(default=False)
    t04 = models.BooleanField(default=False)
    t05 = models.BooleanField(default=False)
    t06 = models.BooleanField(default=False)
    t06 = models.BooleanField(default=False)
    t07 = models.BooleanField(default=False)
    t08 = models.BooleanField(default=False)
    t09 = models.BooleanField(default=False)
    t10 = models.BooleanField(default=False)
    t11 = models.BooleanField(default=False)
    t12 = models.BooleanField(default=False)
    t13 = models.BooleanField(default=False)
    t14 = models.BooleanField(default=False)
    t15 = models.BooleanField(default=False)
    t16 = models.BooleanField(default=False)
    t17 = models.BooleanField(default=False)
    t18 = models.BooleanField(default=False)
    t19 = models.BooleanField(default=False)
    t20 = models.BooleanField(default=False)
    t21 = models.BooleanField(default=False)
    t22 = models.BooleanField(default=False)
    t23 = models.BooleanField(default=False)

    
    
    
    