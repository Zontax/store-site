from re import I
from django.db.models import Prefetch, prefetch_related_objects
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.contrib import auth, messages
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from carts.models import Cart
from orders.models import Order, OrderItem
from users.forms import UserLoginForm, UserRegisterForm, UserProfileForm
from django.core.mail import send_mail
from users.services import generate_code
from users.models import User
from app.settings import EMAIL_HOST_USER, SITE_NAME
from django.core.mail import EmailMessage


def register(request: HttpRequest):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        
        if form.is_valid():
            email = form.cleaned_data.get('email')
            activation_code = generate_code()
            activation_url = request.build_absolute_uri(reverse('user:activate_check', args=[activation_code]))
            
            send_mail(
                subject=f"Код активації акаунта ({SITE_NAME})",
                message=f"""
                    <h2>Код активації акаунта</h2>
                    Код: <b>{activation_code}</b>
                    <p>або перейдіть за посиланням <a href="{activation_url}">{activation_url}</a></p>""",
                from_email=EMAIL_HOST_USER,
                recipient_list=[email,],
                fail_silently=False,
            )
            
            existing_inactive_user = User.objects.filter(email=email, is_active=False).first()
            if existing_inactive_user:
                existing_inactive_user.delete()
                
            existing_active_user = User.objects.filter(email=email, is_active=True).first()
            if existing_active_user:
                messages.success(request, 'Користувач з такою самою адресою email вже зареєстрований і активний.')
                context = {
                    'title': 'Реєстрація',
                    'form': form
                }
                return render(request, 'users/register.html', context)

            # Створення нового користувача з введеною ​​поштою та кодом активації
            user: User = form.save(commit=False)
            user.is_active = False
            user.activation_key = activation_code
            user.save()
            
            # Перенаправлення на сторінку активації
            return redirect(reverse('user:activate'))
    else:
        form = UserRegisterForm()

    context = {
        'title': 'Реєстрація',
        'form': form
    }
    return render(request, 'users/register.html', context)


def activate(request: HttpRequest):
    context = {
        'activaion_text': 'код ',
    }
    return render(request, 'users/activate.html', context)

    
def activate_check(request: HttpRequest, activation_code: str):
    if request.method == 'POST':
        activation_code_post = request.POST['activation_code']
        
        if activation_code_post:
            activation_code = activation_code_post
        
    try:
        user = User.objects.get(activation_key=activation_code)
        
    except User.DoesNotExist:
        messages.success(request, 'Неправильний код активації')
        return redirect(reverse('user:activate'))
    
    except Exception:
        messages.success(request, 'Помилка активації')
        return redirect(reverse('user:activate'))

    user.is_active = True
    user.activation_key = None
    user.save()

    session_key = request.session.session_key
    
    auth.login(request, user)
    
    carts = Cart.objects.filter(session_key=session_key)
    carts.update(user=user)
    carts.update(session_key=None)
    
    messages.success(request, 'Ви успішно зареєструвались та увійшли в акаунт')
    
    return redirect(reverse('user:profile'))


def register_OLD(request: HttpRequest):
    
    if request.method == 'POST':
        form = UserRegisterForm(data=request.POST)
        
        if form.is_valid():
            form.save()
            user: User = form.instance
            session_key = request.session.session_key
            
            auth.login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            
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
        
    orders = (Order.objects.filter(user=request.user)
        .prefetch_related(
            Prefetch('orderitem_set', queryset=OrderItem.objects.select_related('product'))
            ).order_by('-id')
    )

    context = {
        'title': 'Профіль',
        'form': form,
        'orders': orders
    }
    return render(request, 'users/profile.html', context)


def users_cart(request: HttpRequest):
    
    return render(request, 'users/users_cart.html')
