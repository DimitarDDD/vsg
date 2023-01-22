from django.contrib import admin
from django.urls import include, path 
from . import views


app_name = 'authentication'

urlpatterns = [
    path('register', views.register, name='register'),
    path('signin', views.signin, name='signin'),   
    path('signout', views.signout, name='signout'),  
]