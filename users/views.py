from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.contrib import auth, messages, sessions
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from carts.models import Cart
from users.forms import UserLoginForm, UserRegisterForm, UserProfileForm


def login(request: HttpRequest):
    
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        
        if form.is_valid():
            
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            session_key = request.session.session_key
            
            if user:
                auth.login(request, user)
                messages.success(request, f'{request.user.username}, Ви успішно увійшли в акаунт')
                
                if session_key:
                    carts = Cart.objects.filter(session_key=session_key)
                    carts.update(user=user)
                    carts.update(session_key=None)
                
                
                next_url = request.POST.get('next', None)
                
                if next_url and next_url != reverse('user:logout'):  # редірект на бажану сторінку після входу
                    return redirect(next_url)
                    
                return redirect(reverse('main:index'))
    else:
        form = UserLoginForm()

    context = {
        'title': 'Авторизація',
        'form': form
    }
    return render(request, 'users/login.html', context)


def register(request: HttpRequest):
    
    if request.method == 'POST':
        form = UserRegisterForm(data=request.POST)
        
        if form.is_valid():
            form.save()
            user = form.instance
            session_key = request.session.session_key
            
            auth.login(request, user)
            
            carts = Cart.objects.filter(session_key=session_key)
            carts.update(user=user)
            carts.update(session_key=None)
            
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
def logout(request: HttpRequest):
    
    messages.success(request, 'Ви вийшли з акаунта')    
    auth.logout(request)
    return redirect(reverse('main:index'))


@login_required
def profile(request: HttpRequest):
    
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


def users_cart(request: HttpRequest):
    
    return render(request, 'users/users_cart.html')