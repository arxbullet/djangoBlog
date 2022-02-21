from django.shortcuts import render, redirect
from mainapp.forms import RegisterForm

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

            return redirect('index')
    
    return render(request, 'users/register.html', {
        'title': 'registro',
        'form' : register_form
    })