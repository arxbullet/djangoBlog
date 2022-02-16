from django.contrib import admin

from blog.models import Article, Category

# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at', 'updated_at')
    ordering = ('created_at',)

class ArticleAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at', 'updated_at')
    ordering = ('created_at',)


admin.site.register(Article, ArticleAdmin) 
admin.site.register(Category, CategoryAdmin) 

