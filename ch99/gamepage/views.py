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
    model = Game
    template_name = 'gamepage/maingamepage.html'


class GamelistView(ListView):
    model = Game

class NewroomView(CreateView):
    model = Game
    fields=['room_name', 'leader_name', 'people_num']
    success_url = reverse_lazy('list')
    template_name_suffix='_newroom'

class ReadypageView(TemplateView):
    model = Game
    template_name = 'gamepage/readypage.html'
    

