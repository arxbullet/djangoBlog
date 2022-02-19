from django.shortcuts import get_object_or_404, render
from blog.models import Category, Article

# Create your views here.

def articles(request):

    articles = Article.objects.all()

    return render(request, 'articles/list.html', {
        'title' : 'Articulos',
        'articulos' : articles
    })


def category(request, category_id):

    category = get_object_or_404(Category ,id = category_id)
    articles = Article.objects.filter(categories = category_id)
    return render(request, 'categories/category.html', {
        'title' : category,
        'category' : category,
        'articles' : articles
    })