from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
# Create your views here.

def signup(request):
    if request.method == 'POST':
        if request.POST['password'] == request.POST['confirm']:
            user = User.objects.create_user(
                user_id = request.POST['user_id'],
                user_name = request.POST['user_name'],
                user_email = request.POST['user_email'],
                user_pw = request.POST['user_pw']
            )
            auth.login(request, user)
            return redirect('/')