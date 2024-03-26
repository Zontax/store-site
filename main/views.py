from django.http import HttpRequest
from django.views import View
from django.urls import reverse
from django.shortcuts import render, redirect


class IndexView(View):
    
    def get(self, request: HttpRequest):
        return redirect(reverse('catalog:index', kwargs={'category_slug': 'all'}))


class AboutView(View):
    
    def get(self, request: HttpRequest):
        context = {
            'title': 'Про нас',
            'description': 'Це шаблон "Магазин Меблів" (Django 4.2.11)',
        }
        return render(request, 'main/about.html', context)
