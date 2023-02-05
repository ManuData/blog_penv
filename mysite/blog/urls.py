from django.urls import path
from . import views



urlpatterns = [
    path('', views.index, name='index'),
    #path('base', views.base, name='base'),
    path('article/<slug:slug>', views.article, name='article-detail'),
    path('articles', views.articles, name='articles'),


]

