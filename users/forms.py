from django.contrib.auth.forms import AuthenticationForm
from django.forms import ModelForm, CharField, TextInput, PasswordInput
from users.models import User

class UserLoginForm(AuthenticationForm):
    
    username = CharField(label="Ім'я користувача")
    password = CharField(label='Пароль')
    
    class Meta:
        model = User
        fields = ['username', 'password']
        
        
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