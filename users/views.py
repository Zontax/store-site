from django.urls import reverse
from django.contrib import auth
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from users.forms import UserLoginForm, UserRegisterForm
from users.models import User


def login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                return redirect(reverse('main:index'))
    else:
        form = UserLoginForm()

    context = {
        'title': 'Авторизація',
        'form': form
    }
    return render(request, 'users/login.html', context)


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(data=request.POST)
        
        if form.is_valid():
            form.save() # User to DB
            user = form.instance
            auth.login(request, user)
            
            return redirect(reverse('main:index'))
    else:
        form = UserRegisterForm()
        

    context = {
        'title': 'Реєстрація',
        'form': form
    }
    return render(request, 'users/register.html', context)
      
        
def logout(request):
    auth.logout(request)
    return redirect(reverse('main:index'))


def profile(request):
    context = {
        'title': 'Профіль'
    }
    return render(request, 'users/profile.html', context)