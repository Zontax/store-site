from django.urls import reverse
from django.contrib import auth
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from users.forms import UserLoginForm
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
                return HttpResponseRedirect(reverse('main:index'))
    else:
        form = UserLoginForm()

    context = {
        'title': 'Авторизація',
        'form': form
    }
    return render(request, 'users/login.html', context)


def register(request):
    context = {
        'title': 'Register'
    }
    return render(request, 'users/register.html', context)


def profile(request):
    context = {
        'title': 'Profile'
    }
    return render(request, 'users/profile.html', context)\
      
        
def logout(request):
    context = {
        'title': 'Logout'
    }
    return render(request, 'users/logout.html', context)