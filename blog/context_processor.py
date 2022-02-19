from unicodedata import category
from blog.models import Category, Article

def get_categories(request):
    ids_Categories_in_use = Article.objects.filter(public=True).values_list('categories', flat=True)
    categories = Category.objects.filter(id__in = ids_Categories_in_use).values_list('id', 'title')
    return{
        'categories' : categories,
        'ids': ids_Categories_in_use
    }