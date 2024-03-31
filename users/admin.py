from django.contrib import admin

from carts.admin import CartTabAdmin
from orders.admin import OrderTabulareAdmin
from users.models import User

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'is_active', 'first_name', 'last_name', 'email', 'phone_number', 'is_superuser', 'date_joined']
    inlines = [CartTabAdmin, OrderTabulareAdmin]
    search_fields = ['username', 'first_name', 'last_name', 'email', 'phone_number']
    list_filter = ['date_joined', 'last_login']
    readonly_fields = ['username','email', 'phone_number', 'password', 'avatar_image', 'date_joined', 'last_login', 'is_superuser']

    # fields = [
    #     'username',
    #     ('first_name', 'last_name'),
    #     'email',
    #     'phone_number',
    #     'password',
    #     'avatar_image',
    #     'date_joined', 
    #     'last_login',
    # ]