from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Page) #registrar el modelo en panel admin django
title = 'Administrador de paginas'
subtitle = 'proyecto con django'

admin.site.site_header = title
admin.site.site_title = subtitle
admin.site.index_title= subtitle