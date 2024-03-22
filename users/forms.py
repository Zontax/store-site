from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from django.forms import ImageField, CharField, ModelForm, TextInput, PasswordInput, EmailField
from phonenumber_field.formfields import PhoneNumberField
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
    last_name = CharField(required=False)
    username = CharField(label="Ім'я користувача")
    email = EmailField(label="Пошта")
    password1 = CharField(label='Пароль')
    password2 = CharField(label='Повторити пароль')
    
    
class UserProfileForm(UserChangeForm):
    class Meta:
        model = User
        fields = (
            'avatar_image',
            'first_name', 
            'last_name', 
            'username', 
            'email',
            'phone_number',
        )
    
    avatar_image = ImageField(required=False)
    first_name = CharField()
    last_name = CharField(required=False)
    username = CharField()
    email = EmailField()
    phone_number = PhoneNumberField(region="UA")
    