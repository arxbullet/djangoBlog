from django.shortcuts import render
from .models import Page
from django.contrib.auth.decorators import login_required 
# Create your views here.

@login_required(login_url='login')
def pages(request, slug):
    page = Page.objects.get(slug = slug)

    return render(request, 'pages/pages.html', {
        'page':page        
    })