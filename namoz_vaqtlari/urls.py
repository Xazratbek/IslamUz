from django.urls import path
from .views import NamozListView, NamozDetailView

urlpatterns = [
		path('namoz_vaqtlari/',NamozListView.as_view(),name='namoz_vaqtlari_list'),
		path('namoz_vaqtlari/<slug:slug>/',NamozDetailView.as_view(),name='namoz_vaqtlari_detail'),
	]