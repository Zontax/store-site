from django.db.models import CharField, TextField, ImageField
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from django.db import models

from phonenumber_field.modelfields import PhoneNumberField


class User(AbstractUser):
    email = models.EmailField('Пошта Email', unique=True)
    description = TextField('Опис профілю', max_length=500, blank=True, null=True)
    phone_number = PhoneNumberField('Номер телефону', region='UA', blank=True, null=True)
    avatar_image = ImageField('Аватар', upload_to='users_avatar_images', blank=True, null=True)
    activation_key = CharField('Код активації', max_length=80, blank=True, null=True)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    
    class Meta():
        db_table = 'users'
        verbose_name = 'Користувач'
        verbose_name_plural = 'Користувачі'
        ordering = ('date_joined',)
        
        
    def __str__(self):
        return f'{self.first_name} {self.last_name} ({self.username})'
