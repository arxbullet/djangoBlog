from django.urls import path
from . import views

urlpatterns=[
    path('inicio/', views.index, name='index'),
    path('', views.index, name='inicio'),
]