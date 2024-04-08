from django.forms import Form, ImageField, CharField, EmailField, ValidationError
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth import get_user_model

from phonenumber_field.formfields import PhoneNumberField
from django_recaptcha.fields import ReCaptchaField
from users.models import User


User = get_user_model()

class UserLoginForm(AuthenticationForm):    
    username = CharField(label="Пошта Email")
    password = CharField(label='Пароль')
    captcha = ReCaptchaField()

        
class UserRegisterForm(UserCreationForm):    
    first_name = CharField()
    last_name = CharField(required=False)
    username = CharField(label="Ім'я користувача")
    email = EmailField(label="Пошта Email")
    password1 = CharField(label='Пароль')
    password2 = CharField(label='Повторити пароль')
    captcha = ReCaptchaField()
    
    class Meta(UserCreationForm.Meta):
        model = User
        fields = (
            'first_name', 
            'last_name', 
            'username', 
            'email',
            'password1',
            'password2',
            'captcha'
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


class ResetPasswordForm(Form):
    email = EmailField(required=True)


class SetNewPasswordForm(Form):
    password1 = CharField(label='Новий пароль')
    password2 = CharField(label='Повторити пароль')
    captcha = ReCaptchaField()

    def clean_password1(self):
        password1 = self.cleaned_data['password1']
        try:
            validate_password(password1)
        except ValidationError as er:
            self.add_error('password1', er)
        return password1


    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data['password1']
        password2 = cleaned_data['password2']
        
        if password1 and password2 and password1 != password2:
            self.add_error('password2', "Паролі не співпадають")
            
        return cleaned_data
