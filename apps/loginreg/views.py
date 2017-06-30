# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import  User



# Create your views here.
def index(request):
    if request.session.get('id'):
        return redirect('myfriend:index')
    return render(request, 'loginreg/index.html')

def register(request):
    results = User.objects.registerVal(request.POST)
    if not results['status']:
        for error in results['errors']:
            messages.error(request, error)
    else:
        messages.success(request, 'User created, please login.')

    return redirect('login:index')

def login(request):
    results = User.objects.loginVal(request.POST)
    if not results['status']:
        for error in results['errors']:
            messages.error(request, error)
    else:
        request.session['id'] = results['user'].id
        return redirect('myfriend:index')
    return redirect('login:index')


def logout(request):
    request.session.clear()
    messages.success(request, 'Logged Out')
    return redirect('login:index')
