from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
def index(request):
    return render(request, 'chat/chat_base.html', {})

def room(request, room_name):
    return render(request, 'chat/chat_room.html', {
        'room_name': room_name
    })