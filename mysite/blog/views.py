from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
import numpy as np
import pandas as pd
import json


# Datos a modo de test
test_datos = [0,1,2,30,34,21]
serie = pd.Series(test_datos,name="test")
obj = {'test1':1,'test2':2}



# Data Base info Articles: 
from .models import Articles

# Data Base info Images: 
from .models import Image

# Create your views here.

def index(request):

    return render(request,'blog/index.html',{'numbers':serie,"obj_as_json":json.dumps(obj)})

def base(request):
    return render(request,'blog/base.html')


def article(request,slug,pk): # Return one single post/article
    post = get_object_or_404(Articles,pk=pk)
    images = Image.objects.filter(article_id=pk)
    #images = post.image_set.all()
    test = slug
    # Check if able to retrieve data from data base based on slug | Nota importante: Estoy enviando siempre el texto del mismo artículo basado en la variable texto
    texto = Articles.objects.get(slug__exact="datalayer-episodio-1")
    articleDataLayer = Articles.objects.get(pk=pk)
    return render(request,'blog/article.html',{'numbers':serie,"obj_as_json":json.dumps(obj),"test":test,"articleDataLayer":articleDataLayer,"texto":texto,"images":images,})


def articles(request): # Display all the posts/articles
    
    articles = Articles.objects.all()
    return render(request,'blog/articles_model.html',{'articles':articles})
    # Sustituir por serializer si queremos utilizar el API
    serializer = ArticlesSerializer(articles,many=True)
    #return render(request,'blog/articles_model.html',{'articles':serializer.data})



