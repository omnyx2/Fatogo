from django.conf.urls import url, include

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    
    #handling about url of hotel_page
    url(r'(?P<hotel_code>.+)/hotel_main.html/$',views.hotel_main, name='hotel_main'),
#    url(r'hotel_page/hotel_main.html/$',views.hotel_main,  name='hotel_main'),
    url(r'(?P<hotel_code>.+)/hotel_amenity.html', views.hotel_amenity, name='hotel_amenity'),
    url(r'(?P<hotel_code>.+)/hotel_evaluation.html', views.hotel_evaluation, name='hotel_evaluation'),
    url(r'(?P<hotel_code>.+)/hotel_slideshow.html', views.hotel_slideshow, name='hotel_slideshow'),
    url(r'(?P<hotel_code>.+)/hotel_travel_info.html', views.hotel_travel_info, name='hotel_travel_info'),
    #handling about url of bill_page
    url(r'bill_page/bill.html', views.bill, name='bill'),
    url(r'bill_page/thankyou.html', views.thankyou, name='thankyou'),
    

]