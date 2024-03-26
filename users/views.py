from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib import auth, messages
from django.utils.decorators import method_decorator
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.db.models import Prefetch
from django.urls import reverse, reverse_lazy
from django.views import View
from django.views.generic import FormView
from users.forms import UserLoginForm, UserRegisterForm, UserProfileForm, ResetTokenForm
from carts.models import Cart
from orders.models import Order, OrderItem
from users.services import generate_code
from users.models import User
from app.settings import EMAIL_HOST_USER, SITE_NAME


class UserRegisterView(FormView):
    template_name = 'users/register.html'
    form_class = UserRegisterForm
    success_url = reverse_lazy('user:login')
    
    def form_valid(self, form: UserRegisterForm):
        
        email = form.cleaned_data['email']        
        user, created = User.objects.get_or_create(email=email)
        
        if created or user.is_active == False:
            activation_code = generate_code()
            activation_url = self.request.build_absolute_uri(
                reverse_lazy('user:register_confirm', kwargs={ "token": activation_code}))
            
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
            
            user.is_active = False
            user.activation_key = activation_code
            user.first_name = form.cleaned_data['first_name']
            user.last_name = form.cleaned_data['last_name']
            user.username = form.cleaned_data['username']
            user.set_password(form.cleaned_data['password1'])
            user.save()
        
        messages.success(self.request, 'На ваш email надіслано лист з посиланням для підтвердження акаунта')
        return super().form_valid(form)


    def form_invalid(self, form: UserRegisterForm):
        return self.render_to_response(self.get_context_data(form=form))


class UserLoginView(LoginView):
    form_class = UserLoginForm
    template_name = 'users/login.html'
    
    def get_success_url(self):
        return reverse('user:profile')

    
@method_decorator(login_required, name='dispatch')
class UserProfileView(View):
    template_name = 'users/profile.html'
    
    def get(self, request):
        form = UserProfileForm(instance=request.user)
        orders = (Order.objects.filter(user=request.user)
            .prefetch_related(
                Prefetch('orderitem_set', queryset=OrderItem.objects.select_related('product'))
                ).order_by('-id')
        )
        context = {
            'form': form,
            'orders': orders
        }
        return render(request, self.template_name, context)
        
        
    def post(self, request):
        form = UserProfileForm(data=request.POST, instance=request.user, files=request.FILES)
        
        if form.is_valid():
            form.save()
            messages.success(request, 'Дані користувача успішно змінено')           
        
        orders = (Order.objects.filter(user=request.user)
            .prefetch_related(
                Prefetch('orderitem_set', queryset=OrderItem.objects.select_related('product'))
                ).order_by('-id')
        )
        context = {
            'form': form,
            'orders': orders
        }
        return render(request, self.template_name, context)
        
        
        def get_success_url(self):
            return reverse('user:profile')
        
        
        def get_context_data(self):
            
            return context
    

@login_required
def logout(request: HttpRequest):
    
    messages.success(request, 'Ви вийшли з акаунта')    
    auth.logout(request)
    return redirect(reverse('main:index'))


class ResetWaitView(FormView):
    template_name = 'users/reset_wait.html'
    form_class = UserRegisterForm
    success_url = reverse_lazy('user:reset_wait')
    
    def form_valid(self, form: UserRegisterForm):
        # Отримуємо токен з форми
        token = form.cleaned_data['token']
        # Зберігаємо токен у атрибуті об'єкту класу
        self.token = token
        # Викликаємо суперметод form_valid для виконання стандартних дій
        return super().form_valid(form)
    
    
    def get_success_url(self) -> str:
        if hasattr(self, 'token'):
            return reverse('user:register_confirm', kwargs={"token": self.token})
        else:
            return super().get_success_url() 
    

def register_confirm(request: HttpRequest, token: str): 
    try:
        user = User.objects.get(activation_key=token)
        
    except User.DoesNotExist:
        messages.success(request, 'Неправильний код активації або він застарів')
        return redirect(reverse('user:reset_wait'))
    
    except Exception:
        messages.success(request, 'Помилка активації')
        return redirect(reverse('user:reset_wait'))

    user.is_active = True
    user.activation_key = None
    user.save(update_fields=['is_active', 'activation_key'])

    session_key = request.session.session_key
    
    auth.login(request, user)
    
    anonymous_cart_products = Cart.objects.filter(session_key=session_key)
    anonymous_cart_products.update(user=user)
    anonymous_cart_products.update(session_key=None)
    
    messages.success(request, 'Ви успішно зареєструвались та увійшли в акаунт')
    
    return redirect(reverse('user:profile'))


def activate(request: HttpRequest):
    context = {
        'activaion_text': 'код ',
    }
    return render(request, 'users/activate.html', context)


@login_required
def profile(request: HttpRequest):
    ...


def users_cart(request: HttpRequest):
    
    return render(request, 'users/users_cart.html')


def login_OLD(request: HttpRequest):
    
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
