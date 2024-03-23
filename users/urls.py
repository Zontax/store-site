from django.urls import path
from users import views

app_name = 'users'

urlpatterns = [
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    
    path('activate/', views.activate, name='activate'),
    path('activate_check/<str:activation_code>/', views.activate_check, name='activate_check'),
    path('password-reset/', views.test, name='password_reset'),
    
    path('profile/', views.profile, name='profile'),
    path('logout/', views.logout, name='logout'),
    path('users-cart/', views.users_cart, name='users_cart'),
    path('test/', views.test, name='test'),
]
