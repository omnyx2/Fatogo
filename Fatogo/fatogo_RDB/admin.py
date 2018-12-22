# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
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
from .models import CompanyInfomations
from .models import CompanyMasterInfomations
from .models import CompanyAccounts
from .models import CompanyReview
from .models import CompanyAddress
from .models import CompanyAuxiliaryFacilites
from .models import CompanyAroundFacilites
from .models import CompanyInnerRoomFacilites
from .models import CompanyAroundEnvironment

# Register your models here.
@admin.register(CompanyInfomations)
                #CompanyMasterInfomations,
                #CompanyAccounts,
                #CompanyReview,
                #CompanyAddress,
                #CompanyAuxiliaryFacilites,
                #CompanyAroundFacilites,
                #CompanyInnerRoomFacilites,
                #CompanyAroundEnvironment
                
class AdminCompanyInfomations(admin.ModelAdmin):
    list_display = ['identifyCode',
                    'hotelName', 
                    'hotelAvgScore',
                    'hotelTraffic'
                   ]
@admin.register(CompanyMasterInfomations)
class AdminCompanyMasterInfomations(admin.ModelAdmin):
    list_display = ['__unicode__',
                    'masterName',
                    'masterRegistrationNumber',
                    'masterBusinessLicenseNumber',
                    'masterPhoneNumber',
                    'masterEmail'
                    ]
@admin.register(CompanyAccounts)
class AdminCompanyAccounts(admin.ModelAdmin):
    list_display = ['__unicode__',
                    'tid',
                    'password',
                    'authority'
                   ]
@admin.register(CompanyReview)
class AdminCompanyReview(admin.ModelAdmin):
    list_display = ['__unicode__',
                    'comfortableScore',
                    'cleanessScore',
                    'auxiliaryFacilityScore',
                    'newerScore',
                    'avgScore',
                    'reviewedDate',
                    'reviewedGroup',
                   ]
@admin.register(CompanyAddress)    
class AdminCompanyAddress(admin.ModelAdmin):
    list_display = ['__unicode__',
                    'address1',
                    'address2',
                    'address3',
                    'address4',
                    'address5',
                    'address5_1',
                    'address6',
                    'address6_1',
                    'address7',
                    'address8',
                    'addressLatitude',
                    'addressLongitude'
                   ]
@admin.register(CompanyAuxiliaryFacilites)                   
class AdminCompanyAuxiliaryFacilites(admin.ModelAdmin):
    list_display = ['__unicode__',
                    'facilitesName',
                    'facilitesNumber',
                    'oneFacilitesMemberMaxNum',
                    'oneFacilitesMinTimeCell',
                    'priceForOneTimeCell',
                    'serviceStart',
                    'serviceEnd'
                   ]
@admin.register(CompanyAroundFacilites)    
class AdminCompanyAroundFacilites(admin.ModelAdmin):
    list_display = ['__unicode__',
                    'facilitesName',
                    'facilitesExplain',
                    'timeForWalk',
                    'timeForCar',
                    'serviceStart',
                    'serviceEnd'
                   ]
    
@admin.register(CompanyInnerRoomFacilites)
class AdminCompanyInnerRoomFacilite(admin.ModelAdmin):
    list_display = ['__unicode__',
                    'companyInfo_InnerRoomFacilitesFK',
                    'facilitesName',
                    'oneFacilitesMemberMaxNum'
                   ]
@admin.register(CompanyAroundEnvironment)
class AdminCompanyAroundEnvironment(admin.ModelAdmin):
    list_display = ['__unicode__',
                    'EnvironmentName',
                    'EnvironmentExplain',
                    'timeForWalk',
                    'timeForCar',
                    'serviceStart',
                    'serviceEnd'
                    ]
    
    