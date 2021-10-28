from django.conf.urls import url, include
from django.contrib import admin
from django.urls import path
from .views import HomepageView

urlpatterns = [
    path('', HomepageView.as_view(), name='chat_home'),
]