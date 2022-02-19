from django.urls import path
from . import views

urlpatterns=[
    path('articulos', views.articles , name='list'),
    path('categories/<int:category_id>', views.category , name='categories'),
     path('articulo/<int:article_id>', views.article , name='article'),
]