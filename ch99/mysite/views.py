from typing import ClassVar
from django.views.generic.base import TemplateView
from django.views.generic import CreateView
from django.views.generic.detail import DetailView
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.urls import reverse_lazy
from gamepage.models import Game
from django.shortcuts import render

#--- TemplateView
def HomeView(request):
    
    return render(request, 'home.html')
""" class HomeView(TemplateView):
    template_name = 'home.html' """

#--- User Creation
class UserCreateView(CreateView):
    template_name = 'registration/register.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('register_done')

class UserCreateDoneTV(TemplateView):
    template_name = 'registration/register_done.html'
