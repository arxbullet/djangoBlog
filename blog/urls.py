from django.urls import path
from . import views

urlpatterns=[
    path('articulos', views.articles , name='list')
]