# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.views.generic import ListView
import collections

#This is for webpage rendering
from django.shortcuts import render
from django.http import HttpResponse
from django.forms.models import model_to_dict
#List of datamodel

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

#import every models of Company
from fatogo_RDB.models import UserInfo  
from fatogo_RDB.models import CompanyInfomations
from fatogo_RDB.models import CompanyMasterInfomations
from fatogo_RDB.models import CompanyAccounts
from fatogo_RDB.models import CompanyReview
from fatogo_RDB.models import CompanyAddress
from fatogo_RDB.models import CompanyAuxiliaryfacilities
from fatogo_RDB.models import CompanyAroundfacilities
from fatogo_RDB.models import CompanyInnerRoomfacilities
from fatogo_RDB.models import CompanyAroundEnvironment
from fatogo_RDB.models import CompanyRoomTypeInfomations
from fatogo_RDB.models import RoomInfomation
from fatogo_RDB.models import RoomState
from fatogo_RDB.models import AuxiliaryfacilitiesReserveTime


# Create your views here.

def index(request):
    #form = PostForm()
        
    hotel_lists = CompanyInfomations.objects.all()
    context = {}    
    cnt = 0
      
    hotel_data = []
    for hotel in hotel_lists:
        hotel_address = CompanyAddress.objects.get(companyInfo_AddressFK = hotel.identifyCode)
        temp = {
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
        hotel_data.append(temp)


    context = {'hotel_array' : hotel_data}
    return render(request, 'fatogo_RDB/index.html', context)


#hotel_page url setting
def hotel_main(request, hotel_code):
    #making hotel info
    hotel_info = CompanyInfomations.objects.get(identifyCode=hotel_code)
    hotel_checkout_temp = hotel_info.hotelCheckout
    hotel_checkin_temp = hotel_info.hotelCheckin
    
        #making hotelcheckin and hotelchekout time
    if hotel_checkout_temp >= 12:
        hotel_checkout_temp -= 12
        hotel_checkout_temp = 'PM %d:00' % (hotel_checkout_temp)
    else:
        hotel_checkout_temp = 'AM %d:00' % (hotel_checkout_temp)
        
    if hotel_checkin_temp >= 12:
        hotel_checkin_temp -= 12
        hotel_checkin_temp = 'PM %d:00' % (hotel_checkin_temp)
    else:
        hotel_checkin_temp = 'AM %d:00' % (hotel_checkin_temp)    
        

        #making hotel address info object to dict #this is way of 5_1 and 6_1
    hotel_address_temp =  collections.OrderedDict((sorted(CompanyAddress.objects.filter(companyInfo_AddressFK=hotel_code).values()[0].items())))
    hotel_address_tmp = ""
    hotel_longitude_temp = ''
    hotel_latitude_temp = ''
    
    print hotel_address_temp
        #this is way of 5_1 and 6_1
   
    for adrkey,adrval in hotel_address_temp.items():
        if (adrkey == 'address5') or (adrkey == 'address6'):
            continue
        
        elif adrkey == 'address8' or adrkey == 'companyInfo_AddressFK_id' or adrkey =='id':
            continue
        
        elif adrkey == 'addressLongitude':
            hotel_longitude_temp = adrval
            
        elif adrkey == 'addressLatitude':
            hotel_longitude_temp = adrval
            hotel_latitude_temp = adrval
        
        elif adrkey != hotel_code:
            if adrval != 'testasdas':
                hotel_address_tmp = hotel_address_tmp + ' ' + adrval
   
    print hotel_address_temp
    print hotel_address_tmp 
#        #this is way of 5 and 6
#    for adrkey,adrval in hotel_address_temp.items():
#        if (adrkey == 'address5_1') or (adrkey == 'address6_1'):
#            continue
#        elif adrkey == 'address8' or adrkey == 'companyInfo_AddressFK_id' or adrkey =='id':
#           continue
#        elif adrkey != hotel_code:
#            if adrval != 'testasdas':
#                hotel_address_tmp = hotel_address_tmp + ' ' + adrval           
                
    context_info = {
        'hotel_name':hotel_info.hotelName,
        'hotel_avg_score':hotel_info.hotelAvgScore,
        'hotel_total_review':hotel_info.hotelTotalReview,
        'hotel_checkin':hotel_checkin_temp,
        'hotel_checkout':hotel_checkout_temp,
        'hotel_address':hotel_address_tmp,
        'hotel_latitude':hotel_latitude_temp,
        'hotel_longitude':hotel_longitude_temp
    }

    #making hotel room Type
        #calling query sets
    hotel_room_types = CompanyRoomTypeInfomations.objects.filter(companyInfo_RoomTypeInfomationsFK=hotel_code)    
    print hotel_room_types
        #makeking hotelroom inner facilities list
    hotel_room_inner_facilities_arr = []
    context_room_info_arr = []
    context_room_type_arr = []
    context_room_type_dict ={}
        #data struct [(name,num),(),...]
                
    for hotel_room_type in hotel_room_types: 
        #get room inner facilitites
        hotel_room_inner_facilities = CompanyInnerRoomfacilities.objects.filter(companyRoomTypeInfomations_companyInnerRoomfacilitiesFK=hotel_room_type.id)    
        for hotel_room_inner_facilities_temp in hotel_room_inner_facilities:
            #data struct [(name,num),(),...]
            hotel_room_inner_facilities_arr.append((
                hotel_room_inner_facilities_temp.facilitiesName,
                hotel_room_inner_facilities_temp.onefacilitiesMemberMaxNum
            ))
            
        #get room info maiton
        
        room_info_temp = RoomInfomation.objects.filter(companyRoomTypeInfomations_RoomInfomationFK=hotel_room_type.id)
        for room_info_tmp in room_info_temp:
            context_room_info_temp = {
                'room_type_id':hotel_room_type.id,
                'room_num':room_info_tmp.roomNum,
                'room_floor':room_info_tmp.roomFloor,
                'room_height':hotel_room_type.roomHeight,
                'room_width':hotel_room_type.roomWidth,
                'room_position_x':room_info_tmp.startPointX,
                'room_position_y':room_info_tmp.startPointY,               
            }
            context_room_info_arr.append(context_room_info_temp)    
             
        context_room_type_temp = {
            'room_type' : hotel_room_type.roomType,
            'room_size' : hotel_room_type.roomsize,
            'room_price' : hotel_room_type.roomPrice,
            'room_avg_human_num' : hotel_room_type.roomAvgHumanNum,
            'room_max_human_num' : hotel_room_type.roomMaxHumanNum,
            'hotel_room_inner_facilities' : hotel_room_inner_facilities_arr
        }
        context_room_type_temp= dict(((hotel_room_type.id, context_room_type_temp),))
        context_room_type_dict.update(context_room_type_temp)
        
#    printing each values      
#    print "----------------------------------------------------"
#    for arr in context_room_info_arr:
#        print arr 
#    print "------------------------------------------"
#    for arr in  context_room_type_arr:
#        print arr

    #    final context data
    context = {}
    context.update(context_info)    
    context['hotel_room_info'] = context_room_info_arr
    context['hotel_room_type'] = context_room_type_dict

#    #data struct
#    'hotel_name':hotel_info.hotelName,
#    'hotel_avg_score':hotel_info.hotelAvgScore,
#    'hotel_total_review':hotel_info.hotelTotalReview,
#    'hotel_checkin':hotel_checkin_temp,
#    'hotel_checkout':hotel_checkout_temp,
#    'hotel_address':hotel_address_tmp,
#    'hotel_latitude':hotel_latitude_temp,
#    'hotel_longitude':hotel_longitude_temp
#    'hotel_room_type': {'hotel_room_type.id':{
#            'room_type' : hotel_room_type.roomType,
#            'room_size' : hotel_room_type.roomsize,
#            'room_price' : hotel_room_type.roomPrice,
#            'room_avg_human_num' : hotel_room_type.roomAvgHumanNum,
#            'room_max_human_num' : hotel_room_type.roomMaxHumanNum,
#            'hotel_room_inner_facilities' : hotel_room_inner_facilities_arr
#        }
#     }

#    'hotel_room_info':[
#            'room_type_id':hotel_room_type.id,
#            'room_num':room_info_tmp.roomNum,
#            'room_floor':room_info_tmp.roomFloor,
#            'room_height':hotel_room_type.roomHeight,
#            'room_width':hotel_room_type.roomWidth,
#            'room_position_x':room_info_tmp.startPointX,
#            'room_position_y':room_info_tmp.startPointY
#            ]
#    print context.hotel_room_type.iteritems()
#    print context
#    print context.hotel_room_type
   
    
    return render(request, 'hotel_page/hotel_main.html', context)

            
            
def hotel_amenity(request, hotel_code):
    return render(request, 'hotel_page/hotel_amenity.html', {})
def hotel_evaluation(request,hotel_code):
    return render(request, 'hotel_page/hotel_evaluation.html', {})
def hotel_slideshow(request,hotel_code):
    return render(request, 'hotel_page/hotel_slideshow.html', {})
def hotel_travel_info(request,hotel_code):
    return render(request, 'hotel_page/hotel_travel_info.html', {})

#hotel_bill url setting
def bill(request):
    return render(request, 'bill_page/bill.html', {})
def thankyou(request):
    return render(request, 'bill_page/thankyou.html', {})



