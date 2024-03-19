from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.forms import ModelForm, CharField, TextInput, PasswordInput, EmailField
from users.models import User


class UserLoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ['username', 'password']
    
    username = CharField(label="Ім'я користувача")
    password = CharField(label='Пароль')
        
        
class UserRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = (
            'first_name', 
            'last_name', 
            'username', 
            'email',
            'password1',
            'password2'
        )
        
    first_name = CharField()
    last_name = CharField()
    username = CharField(label="Ім'я користувача")
    email = EmailField()
    password1 = CharField(label='Пароль')
    password2 = CharField(label='Повторити пароль')
    
    
        
        
        
        
        
        
        
        
        
        
        
        
    # username = CharField(
    #     label="Ім'я користувача",
    #     widget=TextInput(attrs={"autofocus": True,
    #                                              'class': 'form-control',
    #                                              'placeholder': "Введіть ваше ім'я користувача"}))
    
    # password = CharField(
    #     label="Пароль",
    #     widget=PasswordInput(attrs={"autocomplete": "current-password",
    #                                                  'class': 'form-control',
    #                                                  'placeholder': "Введіть ваш пароль"}),
    # )