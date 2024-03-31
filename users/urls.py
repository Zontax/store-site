from django.urls import include, path
from users.views import UserRegisterView, UserLoginView, UserProfileView, ResetWaitView, UserRegisterConfirmView, PasswordResetView, UserPasswordResetConfirmView, UserLogoutView, UserCartView

app_name = 'users'

urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
    path('profile/', UserProfileView.as_view(), name='profile'),
    path('register_wait/', ResetWaitView.as_view(), name='reset_wait'),
    path('register_confirm/<token>/', UserRegisterConfirmView.as_view(), name='register_confirm'),
    path('password_reset/', PasswordResetView.as_view(), name='password_reset'),
    path('password_reset_confirm/<token>/', UserPasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('cart/', UserCartView.as_view(), name='users_cart'),
    path('', include('django.contrib.auth.urls')),
]   
