from django.urls import path
from . import views

urlpatterns = [
    path('',views.getData),
    path('articlesApi',views.articlesApi,name='testApi'),
]

