from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import auth, messages
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from users.forms import UserLoginForm, UserRegisterForm, UserProfileForm
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
                messages.success(request, f'{request.user.username}, Ви успішно увійшли в акаунт')
                
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
            messages.success(request, 'Ви успішно зареєструвались та увійшли в акаунт')
            
            return redirect(reverse('main:index'))
    else:
        form = UserRegisterForm()
        
    context = {
        'title': 'Реєстрація',
        'form': form
    }
    return render(request, 'users/register.html', context)
      
    
@login_required
def logout(request):
    messages.success(request, 'Ви вийшли з акаунта')    
    auth.logout(request)
    return redirect(reverse('main:index'))


@login_required
def profile(request):
    if request.method == 'POST':
        form = UserProfileForm(data=request.POST, instance=request.user, files=request.FILES)
        
        if form.is_valid():
            form.save() # Update User to DB
            messages.success(request, 'Дані користувача успішно змінено')           
            return redirect(reverse('users:profile'))
    else:
        form = UserProfileForm(instance=request.user)

    context = {
        'title': 'Профіль',
        'form': form
    }
    return render(request, 'users/profile.html', context)