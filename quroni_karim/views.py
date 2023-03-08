from django.shortcuts import render
from .models import Sura,Oyat
from django.views.generic import ListView
from hitcount.views import HitCountDetailView

class SurahListView(ListView):
    model = Sura
    template_name = 'quroni_karim_list.html'

class SurahDetailView(HitCountDetailView):
    model = Oyat
    template_name = 'quroni_karim_detail.html'
    count_hit = True
