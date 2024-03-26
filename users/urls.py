from django.urls import include, path
from users.views import UserRegisterView, UserLoginView, UserProfileView, ResetWaitView, users_cart, register_confirm

app_name = 'users'

urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('profile/', UserProfileView.as_view(), name='profile'),
    path('reset_wait/', ResetWaitView.as_view(), name='reset_wait'),
    path('register_confirm/<token>/', register_confirm, name='register_confirm'),
    path('cart/', users_cart, name='users_cart'),
    path('', include('django.contrib.auth.urls')),
    
    # path('login/', views.login, name='login'),
    # path('activate/', views.activate, name='activate'),
    # path('logout/', views.logout, name='logout'),
]
