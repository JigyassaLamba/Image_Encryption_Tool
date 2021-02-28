from django.contrib import admin 
from django.urls import path 

from . import views
  
urlpatterns = [ 
    path('', views.decryption,name="decryption"), 
    path('result/', views.get_decrypted_image,name="result"), 
] 