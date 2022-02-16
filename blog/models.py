from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User


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
    user = models.ForeignKey(User, verbose_name='usuario', on_delete=models.CASCADE)#si borro un usuario se borram sus articulos 
    categories = models.ManyToManyField(Category,verbose_name='categoria', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True ,verbose_name='Creado el ')
    updated_at = models.DateTimeField(auto_now_add=True ,verbose_name='Actualizado el ')

    class Meta:
        verbose_name='Articulo'
        verbose_name_plural ='Articulos'

    def __str__(self):
        return self.title