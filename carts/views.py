from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import auth, messages
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect


def index(request):
    return render(request, 'carts/index.html')

def cart_add(request, product_id):
    return render(request, 'carts/index.html')


def cart_change(request, product_id):
    return render(request, 'carts/index.html')


def cart_remove(request, product_id):
    return render(request, 'carts/index.html')