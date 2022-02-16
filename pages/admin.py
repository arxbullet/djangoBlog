from django.contrib import admin
from .models import *

# Register your models here.

#config nueva para mi modelo, personalizar busqueda modelos
class pageAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at', 'updated_at')
    search_fields= ('title', 'content')
    list_filter = ('visible',)
    list_display = ('title', 'created_at') 
    ordering = ('created_at')


admin.site.register(Page) #registrar el modelo en panel admin django
title = 'Administrador de paginas'
subtitle = 'proyecto con django'

admin.site.site_header = title
admin.site.site_title = subtitle
admin.site.index_title= subtitle