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
CompanyAuxiliaryFacilites
CompanyAroundFacilites
CompanyInnerRoomFacilites
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
    
    #desired Facilites
    desiredAuxiliaryFacilites = models.CharField(max_length=100)
    desiredInnerFacilites = models.CharField(max_length=100)
    desiredAroundFacilites = models.CharField(max_length=100)
    desiredAroundEnvironment = models.CharField(max_length=100)
    
    
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
    address1 = models.CharField(max_length=100, default='testasdas')
    address2 = models.CharField(max_length=100, default='testasdas')
    address3 = models.CharField(max_length=100, default='testasdas')
    address4 = models.CharField(max_length=100, default='testasdas')
    address5 = models.CharField(max_length=100, default='testasdas')
    address5_1 = models.CharField(max_length=100, default='testasdas')
    address6 = models.CharField(max_length=100, default='testasdas')
    address6_1 = models.CharField(max_length=100, default='testasdas')
    address7 = models.CharField(max_length=100, default='testasdas')
    address8 = models.CharField(max_length=100, default='testasdas')
    
    #위도 경도 정보
    addressLatitude = models.CharField(max_length=100, default='testasdas')
    addressLongitude = models.CharField(max_length=100, default='testasdas') 
    def __unicode__(self):
        return '%s' % self.companyInfo_AddressFK.identifyCode
    
class CompanyAuxiliaryFacilites(models.Model):
    #FK
    companyInfo_AuxiliaryFacilitesFK = models.ForeignKey('CompanyInfomations', on_delete=models.CASCADE)
    #기본정보
    facilitesName = models.CharField(max_length=100, default='testasdas')
    facilitesNumber = models.PositiveSmallIntegerField()
    oneFacilitesMemberMaxNum = models.PositiveSmallIntegerField()
    #단위시간
    oneFacilitesMinTimeCell = models.PositiveSmallIntegerField()
    priceForOneTimeCell = models.IntegerField()
    serviceStart = models.PositiveSmallIntegerField()
    serviceEnd =  models.PositiveSmallIntegerField()
    def __unicode__(self):
        return '%s' % self.companyInfo_AuxiliaryFacilitesFK.identifyCode

class CompanyAroundFacilites(models.Model):
    companyInfo_AroundFacilitesFK = models.ForeignKey('CompanyInfomations', on_delete=models.CASCADE)
    #기본정보 시간은 전부 분단위
    facilitesName = models.CharField(max_length=100, default='testasdas')
    facilitesExplain = models.TextField(max_length=20000, default='testasdas')
    timeForWalk  = models.PositiveSmallIntegerField()
    timeForCar = models.PositiveSmallIntegerField()
    serviceStart = models.PositiveSmallIntegerField()
    serviceEnd =  models.PositiveSmallIntegerField()
    def __unicode__(self):
        return '%s' % self.companyInfo_AroundFacilitesFK.identifyCode  
        

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
    companyInfo_RoomTypeInfomations = models.ForeignKey('CompanyInfomations', on_delete=models.CASCADE)
    roomType = models.CharField(max_length=100, primary_key=True, unique=True, default='testasdas')
    roomWidth = models.PositiveSmallIntegerField(default=0)
    roomHeight = models.PositiveSmallIntegerField(default=0)
    roomPrice = models.IntegerField(default=0)
    roomMaxHumanNum = models.IntegerField(default=3)
    roomAvgHumanNum = models.IntegerField(default=1)
    def __unicode__(self):
        return '%s' %  companyInfo_RoomTypeInfomations.identifyCode
    
    
class CompanyInnerRoomFacilites(models.Model):
    companyInfo_companyRoomFacilitesFK = models.ForeignKey('CompanyInfomations', on_delete=models.CASCADE)
    #기본정보
    companyRoomTypeInfomations_InnerRoomFacilitesFK = models.ForeignKey('CompanyRoomTypeInfomations', on_delete=models.CASCADE)
    #기본정보
    facilitesName = models.CharField(max_length=100, default='testasdas')
    oneFacilitesMemberMaxNum = models.IntegerField() 
    def __unicode__(self):
        return '%s' % self.companyInfo_InnerRoomFacilitesFK.identifyCode
        
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
    
#class reservation_system():
#class credit_info():