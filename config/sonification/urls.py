from .views import *
from django.urls import path
from django.urls import re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

urlpatterns = [
    path('now_data/',now_data, name='now_data'),
    path('day_data/', day_data, name='day_data'),
    path('minute_data/', minute_data, name='minute_data'),
    path('week_data/', week_data, name='week_data'),
    path('data_to_sound/', data_to_sound, name='data_sound'),
    path('my_stocks/', my_stocks, name='my_stocks'),
    path('buy/', buy, name='buy'),
    path('sell/', sell, name='sell'),
]