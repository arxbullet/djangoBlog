from django.shortcuts import render
from .models import Page
# Create your views here.

def pages(request, slug):
    page = Page.objects.get(slug = slug)

    return render(request, 'pages/pages.html', {
        'page':page        
    })