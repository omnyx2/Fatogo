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
CompanyAuxiliaryfacilities
CompanyAroundfacilities
CompanyInnerRoomfacilities
CompanyAroundEnvironment
CompanyRoomTypeInfomations
RoomInfomation
RoomState
"""
from .models import UserInfo
from .models import CompanyInfomations
from .models import CompanyMasterInfomations
from .models import CompanyAccounts
from .models import CompanyReview
from .models import CompanyAddress
from .models import CompanyAuxiliaryfacilities
from .models import CompanyAroundfacilities
from .models import CompanyInnerRoomfacilities
from .models import CompanyAroundEnvironment
from .models import CompanyRoomTypeInfomations
from .models import RoomInfomation
from .models import RoomState
from .models import AuxiliaryfacilitiesReserveTime
# Register your models here.


                

class AdminCompanyMasterInfomations(admin.ModelAdmin):
    list_display = ['__unicode__',
                    'masterName',
                    'masterRegistrationNumber',
                    'masterBusinessLicenseNumber',
                    'masterPhoneNumber',
                    'masterEmail',
                    ]
    

class AdminCompanyAccounts(admin.ModelAdmin):
    list_display = ['__unicode__',
                    'tid',
                    'password',
                    'authority',
                   ]

    
class AdminCompanyReviewInline(admin.TabularInline):
    model = CompanyReview
    pass
#    list_display = ['__unicode__',
#                    'comfortableScore',
#                    'cleanessScore',
#                    'auxiliaryFacilityScore',
#                    'newerScore',
#                    'avgScore',
#                    'reviewedDate',
#                    'reviewedGroup'
#                   ]

    
class AdminCompanyAddressInline(admin.TabularInline):
    model = CompanyAddress
    extra = 1
    pass
#    list_display = ['__unicode__',
#                    'address1',
#                    'address2',
#                    'address3',
#                    'address4',
#                    'address5',
#                    'address5_1',
#                    'address6',
#                    'address6_1',
#                    'address7',
#                    'address8',
#                    'addressLatitude',
#                    'addressLongitude'
#                   ]
class AdminAuxiliaryfacilitiesReserveTimeInline(admin.TabularInline):
    model = AuxiliaryfacilitiesReserveTime
#    t00
#    t01
#    t02
#    t03
#    t04
#    t05
#    t06
#    t06
#    t07
#    t08
#    t09
#    t10
#    t11
#    t12
#    t13
#    t14
#    t15
#    t16
#    t17
#    t18
#    t19
#    t20
#    t21
#    t22
#    t23          
        
class AdminCompanyAuxiliaryfacilities(admin.ModelAdmin):
#    model = CompanyAuxiliaryfacilities
#    pass
    list_display = ['__unicode__',
                    'facilitiesName',
                    'facilitiesNumber',
                    'onefacilitiesMemberMaxNum',
                    'onefacilitiesMinTimeCell',
                    'priceForOneTimeCell',
                    'serviceStart',
                    'serviceEnd'
                   ]
    
    inlines = [AdminAuxiliaryfacilitiesReserveTimeInline]

    
class AdminCompanyAroundfacilitiesInline(admin.TabularInline):
    model = CompanyAroundfacilities
    pass
#    list_display = ['__unicode__',
#                    'facilitiesName',
#                    'facilitiesExplain',
#                    'timeForWalk',
#                    'timeForCar',
#                    'serviceStart',
#                    'serviceEnd',
#                   ]



class AdminCompanyInnerRoomfacilitiesInline(admin.TabularInline):
    model = CompanyInnerRoomfacilities
    pass
#    list_display = ['companyRoomTypeInfomations_companyInnerRoomfacilitiesFK',
#                    'facilitiesName',
#                    'onefacilitiesMemberMaxNum'
#                   ]
    

class AdminCompanyAroundEnvironment(admin.ModelAdmin):
    list_display = ['__unicode__',
                    'EnvironmentName',
                    'EnvironmentExplain',
                    'timeForWalk',
                    'timeForCar',
                    'serviceStart',
                    'serviceEnd',
                    ]
    
class AdminUserInfo(admin.ModelAdmin):
    fields = [
              'kakaoTalkID',
              'tripPerpose',
              'organizationName',
              'startingAreaSI',
              'startingAreaGUUN',
              'startingAreaGU',
              'desiredTripAreaSI',
              'desiredTripAreaGUUN',
              'desiredTripAreaGU',
              'expectMemberNumber'
             ]

    
class AdminRoomState(admin.ModelAdmin):
        
    list_display = [
              'roomReservation_roomStateFK',
              'reservationBlock',
              'reservated',
              'reservatedDate',#예약을 진행했던 날짜
              'reservationFirstDate',
              'reservationEndDate',
              'checkoutTime',
              'checkinTime',
            ]

class AdminRoomInfomationInline(admin.TabularInline):
    model = RoomInfomation
    pass
#    fields = [
#              'roomNum',
#              'roomFloor',
#              'compInfo_RoomInfoFK',
#              'companyRoomTypeInfo_RoomInfoFK',
#              'userInfo_RoomReservationFK',
#              'startPointX',
#              'startPointY',
#             ]

class AdminCompanyInfomations(admin.ModelAdmin):
    list_display = ['identifyCode',
                    'hotelName', 
                    'hotelAvgScore',
                    'hotelTraffic',
                   ]
    
    inlines = [
        AdminCompanyReviewInline,
        AdminCompanyAddressInline, 
#        AdminCompanyAuxiliaryfacilitiesInline, 
        AdminCompanyAroundfacilitiesInline,
    ]
    
class AdminCompanyRoomTypeInfomations(admin.ModelAdmin):
    list_display = ['__unicode__',
                    'roomType',
                    'roomWidth',
                    'roomHeight',
                    'roomPrice',
                    'roomMaxHumanNum',
                    'roomAvgHumanNum',
                    ]
    inlines = [
        AdminCompanyInnerRoomfacilitiesInline, 
        AdminRoomInfomationInline,
    ]


#list of tables    
#UserInfo    
#CompanyInfomations   
#CompanyMasterInfomations
#CompanyAccounts
#CompanyReview
#CompanyAddress
#CompanyAuxiliaryfacilities
#CompanyAroundfacilities
#CompanyInnerRoomfacilities
#CompanyAroundEnvironment
#CompanyRoomTypeInfomations
#CompanyInnerRoomfacilities
#RoomInfomation
#CompanyRoomTypeInfomations
#RoomState


# This is for inline function
#admin.site.register(CompanyInfomations
#admin.site.register(CompanyMasterInfomations
#admin.site.register(CompanyAccounts
admin.site.register(CompanyReview)
admin.site.register(CompanyAddress)
#admin.site.register(CompanyAuxiliaryfacilities)
admin.site.register(CompanyAroundfacilities)
admin.site.register(CompanyInnerRoomfacilities)
#admin.site.register(CompanyAroundEnvironment
admin.site.register(RoomInfomation)
admin.site.register(AuxiliaryfacilitiesReserveTime)
#admin.site.register(RoomState
#admin.site.register(UserInfo


#This is for register Models
admin.site.register(CompanyInfomations, AdminCompanyInfomations)
admin.site.register(CompanyMasterInfomations, AdminCompanyMasterInfomations)
admin.site.register(CompanyAccounts, AdminCompanyAccounts)
#admin.site.register(CompanyReview, AdminCompanyReview)
#admin.site.register(CompanyAddress, AdminCompanyAddress)
admin.site.register(CompanyAuxiliaryfacilities, AdminCompanyAuxiliaryfacilities)
#admin.site.register(CompanyAroundfacilities, AdminCompanyAroundfacilities)
#admin.site.register(CompanyInnerRoomfacilities, AdminCompanyInnerRoomfacilities)
admin.site.register(CompanyAroundEnvironment, AdminCompanyAroundEnvironment)
#admin.site.register(RoomInfomation, AdminRoomInfomation)
admin.site.register(RoomState, AdminRoomState)
#admin.site.register(AuxiliaryfacilitiesReserveTime, AdminAuxiliaryfacilitiesReserveTime)
admin.site.register(UserInfo, AdminUserInfo)   
admin.site.register(CompanyRoomTypeInfomations,AdminCompanyRoomTypeInfomations)
