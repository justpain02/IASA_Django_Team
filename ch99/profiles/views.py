from django.shortcuts import render
from django.contrib.auth.models import User
from django.views.generic.detail import DetailView
# Create your views here.

class ProfileView(DetailView):
    context_object_name = 'profile_user'
    model = User
    template_name = "profiles/profile_user.html"