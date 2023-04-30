from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
import json


# Data Base info Articles: 
from .models import Articles

# Data Base info Images: 
from .models import Image


# Forms

from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.template import RequestContext

from .forms import NameForm



# Create your views here.

def index(request):
    # DataLayer
    dl = {'pagePath':request.path,'pageCategory':'home'}
    pageUrl = request.path
    response = render(request,'blog/index.html',{'dataLayer':dl})
    response.set_cookie('TEST', 'PUTO AMO !!')
    return response
 

def base(request):
    return render(request,'blog/base.html')


def article(request,slug,pk): # Return one single post/article

    articleBody = Articles.objects.get(pk=pk)
    articleDataLayer = Articles.objects.get(pk=pk)
    articleLength = str(len(Articles.objects.get(pk=pk).body))

    # Test cookie
    #DataLayer
    
    dl = {'pagePath':request.path,
          'pageCategory':'articles',
          'articleTitle':articleDataLayer.title,
          'articleId':articleDataLayer.id,
          'articleCategory':articleDataLayer.article_category,
          'articleLength':articleLength,
          'articleTags':articleDataLayer.tags}

    post = get_object_or_404(Articles,pk=pk)
    images = Image.objects.filter(article_id=pk)
    # Check if able to retrieve data from data base based on slug | Nota importante: Estoy enviando siempre el texto del mismo artículo basado en la variable texto
   
    return render(request,'blog/article.html',{"texto":articleBody,"images":images,'dataLayer':dl})


def articles(request): # Display all the posts/articles
    dl = {'pagePath':request.path,'pageCategory':'articles'}
    articles = Articles.objects.all()
    return render(request,'blog/articles_model.html',{'articles':articles,'dataLayer':dl})
  


def get_name(request):
     # if this is a POST request we need to process the form data
    if request.method == "POST":
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            print(form)
            data = form.cleaned_data['name']
            return HttpResponse("dato was created with value"+data)

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()

    return render(request, "blog/test.html", {"form": form})