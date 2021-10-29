from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from .views import *

urlpatterns = [
    path('', GamelistView.as_view(), name='list'),
    path('mainpage/<int:pk>/', MainpageView.as_view(), name='maingamepage'),
    path('add/', NewroomView.as_view(), name='add'),
    path('ready/<int:pk>/', ReadypageView.as_view(), name='ready'),
]