from django.contrib import admin 
from django.urls import path 

from . import views
  
urlpatterns = [ 
    path('', views.encryption,name="home"), 
    path('result/', views.get_encrypted_image,name="result"), 
] 