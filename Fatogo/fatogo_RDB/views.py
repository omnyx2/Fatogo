# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request, 'fatogo_RDB/index.html',{})


#2.hotel_page url setting
def hotel_1(request):
    return render(request, '2.hotel_page/hotel_1.html')