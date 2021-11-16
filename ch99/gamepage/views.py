from django.shortcuts import redirect, render
from typing import ClassVar
from django.views.generic.base import TemplateView
from django.views.generic import CreateView
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.urls import reverse_lazy
from .models import Game
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
#--- TemplateView
class MainpageView(DetailView):
    model = Game
    template_name = 'gamepage/maingamepage.html'


class GamelistView(ListView):
    model = Game
    template_name_suffix='_list'

class NewroomView(CreateView):
    model = Game
    fields=['room_name', 'leader_name']
    success_url = reverse_lazy('list')
    template_name_suffix='_newroom'

class ReadypageView(DetailView): # DetailView로 하면 pk를 object로 불러오는게 가능하다
    model = Game
    template_name = 'gamepage/readypage.html'
    
@login_required
def join(request, Game_id):
    game = get_object_or_404(Game, id=Game_id)
    if request.user in game.people_num.all():
        game.people_num.remove(request.user)
        return redirect('/gamepage/')
    else:
        game.people_num.add(request.user)
        return redirect(f'/gamepage/ready/{Game_id}/')
    
