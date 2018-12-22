# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request, 'fatogo_RDB/index.html',{})

def hotel_page(request):
    return render(response, 'fatogo_RDB/2.hotel_page/hotel_1.html',{})

