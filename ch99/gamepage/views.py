from django.shortcuts import render
from typing import ClassVar
from django.views.generic.base import TemplateView
from django.views.generic import CreateView
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.urls import reverse_lazy

#--- TemplateView
class MainpageView(TemplateView):
    template_name = 'gamepage/maingamepage.html'