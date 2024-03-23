from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from django.forms import ModelForm, ImageField, CharField, TextInput, PasswordInput, EmailField, ValidationError
from phonenumber_field.formfields import PhoneNumberField
from django.contrib.auth.password_validation import validate_password
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
    
    
    def clean_password2(self):
        password2 = super().clean_password2()  # Викликаємо стандартний метод clean_password2()

        # Додаткові перевірки
        # Наприклад, перевірка довжини пароля
        if len(password2) < 8:
            raise ValidationError("Пароль повинен містити щонайменше 8 символів", code='password_too_short')

        return password2
    
    
    
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
    