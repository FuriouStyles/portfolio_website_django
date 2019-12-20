from django.urls import path
from . import views
from datetime import datetime


urlpatterns = [
    path('', views.boxing, name='boxing_landing'),
    #path('about/', views.about, name='about'),
    #path('blog/', views.blog, name='blog-home')
] 
