# -*- coding: utf-8 -*-
from __future__ import unicode_literals

#form, post handling


#This is for webpage rendering
from django.shortcuts import render
from django.http import HttpResponse

#import every models of Company
from .models import CompanyInfomations
from .models import CompanyMasterInfomations
from .models import CompanyAccounts
from .models import CompanyReview
from .models import CompanyAddress
from .models import CompanyAuxiliaryFacilites
from .models import CompanyAroundFacilites
from .models import CompanyInnerRoomFacilites
from .models import CompanyAroundEnvironment

# Create your views here.

def index(request):
    #form = PostForm()
    hotel_Infomation_list = CompanyInfomations.objects.all()
    #chang filter to get
    hotel_Address_parts = CompanyAddress.objects.filter(companyInfo_AddressFK=hotel_Infomation_list)
    context = {
                'hotel_infomation_list':hotel_Infomation_list,
                'hotel_address_parts': hotel_Address_parts
              }
    return render(request, 'fatogo_RDB/index.html', context)


#hotel_page url setting

def hotel_main_test(request, hotel_name):
    hotel_Infomation_list = CompanyInfomations.objects.all()
    hotel_name = hotel_Infomation_list.values()[1]
    return render(request, 'hotel_page/hotel_main.html')

def hotel_main(request):
    return render(request, 'hotel_page/hotel_main.html', {})


def hotel_amenity(request):
    return render(request, 'hotel_page/hotel_amenity.html', {})
def hotel_evaluation(request):
    return render(request, 'hotel_page/hotel_evaluation.html', {})
def hotel_slideshow(request):
    return render(request, 'hotel_page/hotel_slideshow.html', {})
def hotel_travel_info(request):
    return render(request, 'hotel_page/hotel_travel_info.html', {})

#hotel_bill url setting
def bill(request):
    return render(request, 'bill_page/bill.html', {})
def thankyou(request):
    return render(request, 'bill_page/thankyou.html', {})



