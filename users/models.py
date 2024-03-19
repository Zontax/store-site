from django.db import models
from django.db.models import Model, CharField, SlugField, TextField, ImageField, DecimalField, PositiveIntegerField, ForeignKey
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    avatar_image = ImageField(upload_to='users_avatar_images', blank=True, null=True, verbose_name='Аватар')
    
    class Meta():
        db_table = 'users'
        verbose_name = 'Користувач'
        verbose_name_plural = 'Користувачі'
        ordering = ('id',)
        
    def __str__(self):
        is_admin: str = ''
        if self.is_superuser:
            is_admin = '- ADMIN'
        return f'{self.first_name} {self.last_name} ({self.username}) {is_admin}'