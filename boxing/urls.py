from django.urls import path
from . import views
from datetime import datetime


urlpatterns = [
    path('', views.boxing, name='boxing_landing'),
    path('boxing_long_form/', views.boxing_long_form, name='boxing_long_form')
]
