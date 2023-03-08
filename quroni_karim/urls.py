from django.urls import path
from .views import SurahDetailView, SurahListView

urlpatterns = [
		path('suralar/',SurahListView.as_view(),name='suralar_list'),
		path('suralar/<int:pk>/',SurahDetailView.as_view(),name='suralar_detail'),
	]