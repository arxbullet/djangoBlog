from email.policy import default
from django.db import models
from ckeditor.fields import RichTextField


# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=50, verbose_name='Categoria')
    description = models.CharField(max_length=50, verbose_name='Descripcion')
    created_at = models.DateTimeField(auto_now_add=True ,verbose_name='Creada el ')
    updated_at = models.DateTimeField(auto_now_add=True ,verbose_name='Actualizada el ')
    
    class Meta:
        verbose_name='Categoria'
        verbose_name_plural ='Categorias'

    def __str__(self):
        return self.title


class Article(models.Model):
    title = models.CharField(max_length=50, verbose_name='Titulo')
    content = RichTextField( verbose_name='Contenido')
    image = models.ImageField(default='null', verbose_name='Imagen')
    public = models.BooleanField(verbose_name='visible')
    created_at = models.DateTimeField(auto_now_add=True ,verbose_name='Creado el ')
    updated_at = models.DateTimeField(auto_now_add=True ,verbose_name='Actualizado el ')

    class Meta:
        verbose_name='Articulo'
        verbose_name_plural ='Articulos'

    def __str__(self):
        return self.title