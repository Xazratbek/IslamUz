from django.shortcuts import render
from .models import NamozVaqtlari
from django.views.generic import ListView
from hitcount.views import HitCountDetailView

class NamozListView(ListView):
    model = NamozVaqtlari
    template_name = 'namoz_vaqtlari_list.html'

class NamozDetailView(HitCountDetailView):
    model = NamozVaqtlari
    template_name = 'namoz_vaqtlari_detail.html'
    count_hit = True