from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('search_anime', views.search_anime, name='search_anime'),
]
