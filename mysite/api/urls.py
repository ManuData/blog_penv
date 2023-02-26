from django.urls import path
from . import views

urlpatterns = [
    path('',views.getData),
    path('articlesApi',views.articlesApi,name='testApi'),
    path('article/<slug:slug>/<int:pk>', views.articleApi,name='test'),
]

