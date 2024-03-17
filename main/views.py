from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    context = {
        'title': 'Головна',
        'content': 'Шаблон (Django 4.2.11)',
        'description': '',
        'list': ['first', 'second'],
        'dict': { 'first': 1, 'second': 2},
        'bool': True,
    }
    
    return render(request, 'main/index.html', context)


def about(request):
    context = {
        'title': 'Головна',
        'content': 'Про нас',
        'description': 'Це сайт магазину меблів',
        'list': ['first', 'second'],
        'dict': { 'first': 1, 'second': 2},
        'bool': True,
    }
    
    return render(request, 'main/index.html', context)


def test(request):
    return HttpResponse("Test Page")