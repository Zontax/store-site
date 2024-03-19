from django.http import HttpResponse
from django.urls import reverse
from django.shortcuts import render, redirect


def index(request):
    context = {
        'content': 'Шаблон "Магазина Меблів" (Django 4.2.11)',
        'description': '',
        'list': ['first', 'second'],
        'dict': { 'first': 1, 'second': 2},
        'bool': True,
    }
    
    return redirect(reverse('catalog:index', kwargs={'category_slug': 'all'}))
    return render(request, 'main/index.html', context)


def about(request):
    context = {
        'title': 'Про нас',
        'content': 'Про нас',
        'description': 'Це сайт магазину меблів',
        'list': ['first', 'second'],
        'dict': { 'first': 1, 'second': 2},
        'bool': True,
    }
    
    return render(request, 'main/index.html', context)


def test(request):
    return HttpResponse("Test Page")