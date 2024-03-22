from django.db.models import Model, CharField, SlugField, TextField, ImageField, DecimalField, PositiveIntegerField, ForeignKey
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    email = models.EmailField(unique=True, verbose_name='Email')
    description = TextField(max_length=500, blank=True, null=True, verbose_name='Опис профілю')
    phone_number = PhoneNumberField(region='UA', blank=True, null=True, verbose_name='Номер телефону')
    avatar_image = ImageField(upload_to='users_avatar_images', blank=True, null=True, verbose_name='Аватар')

    
    class Meta():
        db_table = 'users'
        verbose_name = 'Користувач'
        verbose_name_plural = 'Користувачі'
        ordering = ('id',)
        
        
    def __str__(self):
        return f'{self.first_name} {self.last_name} ({self.username})'
