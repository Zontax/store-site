from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from django.forms import Form, ModelForm, ImageField, CharField, TextInput, PasswordInput, EmailField, ValidationError
from captcha.fields import CaptchaField
from phonenumber_field.formfields import PhoneNumberField
from django.contrib.auth.password_validation import validate_password
from users.models import User

User = get_user_model()

class UserLoginForm(AuthenticationForm):    
    username = CharField(label="Пошта Email")
    password = CharField(label='Пароль')

        
class UserRegisterForm(UserCreationForm):    
    first_name = CharField()
    last_name = CharField(required=False)
    username = CharField(label="Ім'я користувача")
    email = EmailField(label="Пошта Email")
    password1 = CharField(label='Пароль')
    password2 = CharField(label='Повторити пароль')
    # captcha = CaptchaField(label='Введіть текст з рисунка')
    
    class Meta(UserCreationForm.Meta):
        model = User
        fields = (
            'first_name', 
            'last_name', 
            'username', 
            'email',
            'password1',
            'password2',
            # 'captcha'
        )
    
    
class UserProfileForm(UserChangeForm):
    avatar_image = ImageField(required=False)
    first_name = CharField()
    last_name = CharField(required=False)
    username = CharField()
    email = EmailField(disabled=True)
    phone_number = PhoneNumberField(region="UA", required=False)
    
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


class ResetTokenForm(Form):
    token = CharField(required=True)
