import re
from django.shortcuts import render, redirect
from mainapp.forms import RegisterForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

# Create your views here.

def index(request):
    return render(request, 'mainapp/index.html', {
        'title':'inicio'
    })

def about(request):
    return render(request, 'mainapp/about.html', {
        'title': 'sobre nosotros'
    })

def register_page(request):

    register_form= RegisterForm()

    if request.method == 'POST' :
        register_form= RegisterForm(request.POST)

        if register_form.is_valid():

            register_form.save()

            messages.success(request, 'te has registrado correctamente')

            return redirect('index')
    
    return render(request, 'users/register.html', {
        'title': 'registro',
        'form' : register_form
    })

def login_page(request):

    if request.method == 'POST' :
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username , password=password)
        if user is not None:
            login(request, user)

            return redirect('index')

        else :  messages.error(request, 'usuario incorrecto')
    
    return render(request, 'users/login.html', {
        'title': 'Login'
    })

def logout_user(request):
    logout(request)
    return redirect('login')