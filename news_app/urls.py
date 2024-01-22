from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('articles/<str:user>/', views.articles, name='articles'),
]
