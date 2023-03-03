from django.shortcuts import render
import requests
from lxml import html
from .models import Iymon, Zakot ,Namoz, Ruza, Haj
from django.views.generic import ListView
from hitcount.views import HitCountDetailView

def islamic_date_time(request):
    url = "https://islom.uz/lotin"
    xpath = '//*[@id="large_screen"]/div/div[1]/div/div/div/div[1]'
    response = requests.get(url)
    byte_string = response.content
    source_code = html.fromstring(byte_string)
    tree = source_code.xpath(xpath)
    result = tree[0].text_content()
    return render(request, 'base.html',context={"islamic_date_time": result})

def index(request):
    return render(request, 'home.html')

class IymonListView(ListView):
    model = Iymon
    template_name = 'iymon_list.html'

class IymonDetailView(HitCountDetailView):
    model = Iymon
    template_name = 'iymon.html'
    count_hit = True

class ZakotListView(ListView):
    model = Zakot
    template_name = 'zakot_list.html'

class ZakotDetailView(HitCountDetailView):
    model = Zakot
    template_name = 'zakot.html'
    count_hit = True

class NamozListView(ListView):
    model = Namoz
    template_name = 'namoz_list.html'

class NamozDetailView(HitCountDetailView):
    model = Namoz
    template_name = 'namoz.html'
    count_hit = True

class RuzaListView(ListView):
    model = Ruza
    template_name = 'ruza_list.html'

class RuzaDetailView(HitCountDetailView):
    model = Ruza
    template_name = 'ruza.html'
    count_hit = True

class HajListView(ListView):
    model = Haj
    template_name = 'haj_list.html'

class HajDetailView(HitCountDetailView):
    model = Haj
    template_name = 'haj.html'
    count_hit = True