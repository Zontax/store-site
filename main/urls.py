from django.urls import path
from django.views.decorators.cache import cache_page
from main import views

app_name = 'main'

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', cache_page(60)(views.about), name='about'),
]
