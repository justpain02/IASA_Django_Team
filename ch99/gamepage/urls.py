from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from django.conf.urls.static import static
from django.conf import settings
from .views import *
from .models import Game

urlpatterns = [
    path('', GamelistView.as_view(), name='list'),
    path('mainpage/<int:pk>/', MainpageView.as_view(), name='maingamepage'),
    path('add/', NewroomView.as_view(), name='add'),
    path('ready/<int:pk>/', ReadypageView, name='ready'),
    path('join/<int:Game_id>/', join ,name='join'),
    path('delete/<int:pk>/',Gamedelete.as_view(),name='delete'),
    url(r'^game_button/$', about_button_status, name="game_button"),
    url(r'^game_check/$', game_check, name="game_check"),
]