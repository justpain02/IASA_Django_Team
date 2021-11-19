from django.shortcuts import redirect, render
from typing import ClassVar
from django.views.generic.base import TemplateView
from django.views.generic import CreateView
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.views.generic.detail import DetailView
from django.views.generic.edit import DeleteView
from django.views.generic.list import ListView
from django.urls import reverse_lazy, reverse
from .models import Game
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse , HttpResponseRedirect
#--- TemplateView
class MainpageView(DetailView):
    model = Game
    template_name = 'gamepage/maingamepage.html'


class GamelistView(ListView):
    model = Game
    template_name_suffix='_list'

""" def NewroomView(request):
    if request.method == "POST":
        room_name = request.POST.get('room_name', None)
        leader_name= request.POST.get('leader_name', None)
        game= Game( room_name=room_name, leader_name=leader_name)
        game.save()
        newroom= Game.objects.all()
        return HttpResponseRedirect(reverse('ReadypageView',kwargs={'pk':newroom[-1].id}))
 """
class NewroomView(CreateView):
    model = Game
    fields=['room_name', 'leader_name']
    template_name_suffix='_newroom'
    success_url= reverse_lazy('list')

def ReadypageView(request, pk):
    game = Game.objects.get(pk=pk)
    return render(request, 'gamepage/readypage.html' ,{'game' : game })

    
""" class ReadypageView(DetailView): # DetailView로 하면 pk를 object로 불러오는게 가능하다
    model = Game
     """

class Gamedelete(DeleteView):
    model = Game
    template_name_suffix='_delete'
    success_url= reverse_lazy('list')
        
@login_required
def join(request, Game_id):
    game = get_object_or_404(Game, id=Game_id)
    if request.user in game.people_num.all():
        game.people_num.remove(request.user)
        return redirect('/gamepage/')
    else:
        game.people_num.add(request.user)
        return redirect(f'/gamepage/ready/{Game_id}/')
    


    
