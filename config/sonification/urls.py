from .views import *
from django.urls import path
from django.urls import re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

urlpatterns = [
    path('transaction_rank/',transaction_rank, name='transaction_rank'),
    path('f_transaction_rank/',f_transaction_rank, name='f_transaction_rank'),
    path('now_data/',now_data, name='now_data'),
    path('f_now_data/',f_now_data, name='f_now_data'),
    path('day_data/', day_data, name='day_data'),
    path('a_day_data/', a_day_data, name='a_day_data'),
    path('f_day_data/', f_day_data, name='f_day_data'),
    path('minute_data/', minute_data, name='minute_data'),
    path('hmm__minute_data/', hmm__minute_data, name='hmm__minute_data'),
    path('a_minute_data/', a_minute_data, name='a_minute_data'),
    path('f_a_day_data/', f_a_day_data, name='f_a_day_data'),
    path('f_a_minute_data/', f_a_minute_data, name='f_a_minute_data'),
    path('f_minute_data/', f_minute_data, name='f_minute_data'),
    path('week_data/', week_data, name='week_data'),
    path('a_week_data/', a_week_data, name='a_week_data'),
    path('f_a_week_data/', f_a_week_data, name='f_a_week_data'),
    path('f_week_data/', f_week_data, name='f_week_data'),
    path('data_to_sound/', data_to_sound, name='data_sound'),
    path('user_info/', user_info, name='user_info'),
    path('buy/', buy, name='buy'),
    path('sell/', sell, name='sell'),
    path('speech_to_text/', speech_to_text, name='speech_to_text'),
    path('like_stock/', like_stock, name='like_stock'),
    path('checkislike/',CheckIsLike.as_view()),
]