from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'2.hotel_page/hotel_1.html', views.hotel_1, name='hotel_1')
]