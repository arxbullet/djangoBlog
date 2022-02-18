from unicodedata import category
from blog.models import Category

def get_categories(request):
    categories = Category.objects.values_list('id', 'title')
    return{
        'categories' : categories
    }