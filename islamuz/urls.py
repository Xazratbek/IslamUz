from django.urls import path
from .views import *

urlpatterns = [
    path('',islamic_date_time, name='home'),
    path('home/',index),
    path('iymon/',IymonListView.as_view(), name='iymon_list'),
    path('iymon/<slug:slug>/',IymonDetailView.as_view(), name='iymon_detail'),
    path('zakot/',ZakotListView.as_view(), name='zakot_list'),
    path('zakot/<slug:slug>/',ZakotDetailView.as_view(), name='zakot_detail'),
    path('namoz/',NamozListView.as_view(), name='namoz_list'),
    path('ruza/',RuzaListView.as_view(), name='ruza_list'),
    path('ruza/<slug:slug>/',RuzaDetailView.as_view(), name='ruza_detail'),
    path('haj/',HajListView.as_view(), name='haj_list'),
    path('haj/<slug:slug>/',HajDetailView.as_view(), name='haj_detail'),
]
