# -*- coding: utf-8 -*-
from __future__ import unicode_literals


from django.views.generic import ListView

#This is for webpage rendering
from django.shortcuts import render
from django.http import HttpResponse

#import every models of Company
from fatogo_RDB.models import CompanyInfomations
from fatogo_RDB.models import CompanyMasterInfomations
from fatogo_RDB.models import CompanyAccounts
from fatogo_RDB.models import CompanyReview
from fatogo_RDB.models import CompanyAddress
from fatogo_RDB.models import CompanyAuxiliaryFacilites
from fatogo_RDB.models import CompanyAroundFacilites
from fatogo_RDB.models import CompanyInnerRoomFacilites
from fatogo_RDB.models import CompanyAroundEnvironment




# Create your views here.

def index(request):
    #form = PostForm()
        
    hotel_lists = CompanyInfomations.objects.all()
    context = {}    
    cnt = 0
    
    for hotel in hotel_lists :
                
        hotel_address = CompanyAddress.objects.get(companyInfo_AddressFK = hotel.identifyCode )
                
        context_temp = {
            'hotel_name' : hotel.hotelName,
            'hotel_code' : hotel.identifyCode,
            'hotel_address1' : hotel_address.address1,
            'hotel_address3' : hotel_address.address3,
#            'hotel_main_imgdir' : '',
#            'hotel_main_emojidir' : '', 
            'hotel_score' : hotel.hotelAvgScore,
            'hotel_reivew_number' : hotel.hotelTotalReview,
            'hotel_price' : '350,000'
        }
        context.update(((hotel.identifyCode,context_temp),))
    
    arr = []
    for hotel in hotel_lists:
        hotel_address = CompanyAddress.objects.get(companyInfo_AddressFK = hotel.identifyCode )
        temp = {
            'hotel_name' : hotel.hotelName,
            'hotel_name' : hotel.hotelName,
            'hotel_code' : hotel.identifyCode,
            'hotel_address1' : hotel_address.address1,
            'hotel_address3' : hotel_address.address3,
#            'hotel_main_imgdir' : '',
#            'hotel_main_emojidir' : '', 
            'hotel_score' : hotel.hotelAvgScore,
            'hotel_review_number' : hotel.hotelTotalReview,
            'hotel_price' : '350,000'
        }
        print(temp)
        arr.append(temp)

    print (arr)
    context = {'array' : arr}
    print(context)
    return render(request, 'fatogo_RDB/index.html', context)


#hotel_page url setting
def hotel_main(request, hotel_code):
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



