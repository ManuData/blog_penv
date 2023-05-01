from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
import json


# Data Base info Articles: 
from .models import Articles

# Data Base info Images: 
from .models import Image


# Forms

from .models import Post
from django.http import JsonResponse


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
  

# For Ajax request
'''
def create_post(request):
    response_data = {}
    if request.POST.get('action') == 'post':
        title = request.POST.get('title')
        description = request.POST.get('description')
        response_data['title'] = title
        response_data['description'] = description
    
        return JsonResponse(response_data)

    #return render(request, 'blog/test.html', {'posts':posts})
    return render(request, 'blog/test.html', {'response_data':response_data})

'''

def create_post(request):
    response_data = {}
    if request.POST.get('action') == 'post':
        
        title = request.POST.get('title')
        description = request.POST.get('description')

        response_data['title'] = title
        response_data['description'] = description
       
        return JsonResponse(response_data)
    return render(request, 'blog/test.html',{'response_data':response_data})






'''
def create_post(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')

        response_data = {}
        response_data['title'] = title
        response_data['description'] = description
       
        return HttpResponse(
            json.dumps(response_data),
            content_type="application/json"
        )
    else:
        return HttpResponse(
            json.dumps({"nothing to see": "this isn't happening"}),
            content_type="application/json"
        )

        '''

    






    
'''Post.objects.create(
    title = title,
    description = description,)'''