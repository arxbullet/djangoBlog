from django.shortcuts import render
from blog.models import Category, Article

# Create your views here.

def articles(request):

    articles = Article.objects.all()

    return render(request, 'articles/list.html', {
        'title' : 'Articulos',
        'articulos' : articles
    })