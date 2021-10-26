from django.urls import path
from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from .views import ProfileView
urlpatterns = [
    path('<int:pk>/', login_required(ProfileView.as_view()), name='profile'),
]