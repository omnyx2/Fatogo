from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^$',views.hotel_page, name='hotel_page_page'),
]