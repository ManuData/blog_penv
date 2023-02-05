from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
import numpy as np
import pandas as pd
import json

# Datos a modo de test
test_datos = [0,1,2,30,34,21]
serie = pd.Series(test_datos,name="test")
obj = {'test1':1,'test2':2}

# Data Base info: 
from .models import Articles


# Create your views here.


def index(request):
    return render(request,'blog/index.html',{'numbers':serie,"obj_as_json":json.dumps(obj)})

def base(request):
    return render(request,'blog/base.html')


def article(request,slug): # Return one single post/article
    test = slug;
    texto = Articles.objects.get(slug__exact="datalayer-episodio-1")
    return render(request,'blog/article.html',{'numbers':serie,"obj_as_json":json.dumps(obj),"test":test,"texto":texto})


def articles(request): # Display all the posts/articles
    articles = Articles.objects.all()
    return render(request,'blog/articles_model.html',{'articles':articles})





