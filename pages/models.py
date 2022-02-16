from django.db import models

# Create your models here.

class Page(models.Model):
    title = models.CharField(max_length=50, verbose_name='Titulo')
    content = models.TextChoices( verbose_name='Contenido')
    slug = models.CharField(max_length=150, verbose_name='URL', unique=True)
    public = models.BooleanField(verbose_name='visible')
    created_at = models.DateTimeField(auto_now_add=True ,verbose_name='Creado el ')
    updated_at = models.DateTimeField(auto_now_add=True ,verbose_name='Actualizado el ')

    class Meta:
        verbose_name='Pagina'
        verbose_name_plural ='Paginas'

    def __str__(self):
        return self.title