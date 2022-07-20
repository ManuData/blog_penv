from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('base', views.base, name='base'),
    path('search/', views.search_results, name='search_results'),
]