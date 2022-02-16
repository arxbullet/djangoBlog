from django.urls import path
from . import views

urlpatterns=[
    path('articles/<str:slug>', views.articles , name='list')
]