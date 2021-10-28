from django.shortcuts import render
from typing import ClassVar
from django.views.generic.base import TemplateView
from django.views.generic import CreateView
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.views.generic.list import ListView
from django.urls import reverse_lazy
from .models import Game

#--- TemplateView
class MainpageView(TemplateView):
    template_name = 'gamepage/maingamepage.html'


class Gamelist(ListView):
    model = Game

