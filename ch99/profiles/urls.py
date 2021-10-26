from django import views
from django.urls import path
from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from django.views.generic.base import View
from .views import ProfileView, ProfileUpdateView

# 참고 : https://ldgeao99.tistory.com/118, https://ldgeao99.tistory.com/119
urlpatterns = [
    path('<int:pk>/', login_required(ProfileView.as_view()), name='profile'),
    path('profile_update/', login_required(ProfileUpdateView.as_view()), name='profile_update')
]