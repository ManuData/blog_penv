from rest_framework.response import Response
from rest_framework.decorators import api_view
from blog.models import Articles
from .serializers import ArticlesSerializer,ArticlesListSerializer
from django.shortcuts import get_object_or_404, render
from rest_framework.reverse import reverse



@api_view(['GET'])
def getData(request):
    #person = {'name':'Manu','age':32}
    articles = Articles.objects.all()
    serializer = ArticlesSerializer(articles,many=True)
    #return Response(serializer.data)
    #return render(request,'blog/test.html',{'articles':serializer.data,"url-to-article":reverse('article-detail',request=request)})
    #return Response(serializer.data)
    #return Response({'article-detail': reverse('article-detail',request=request)})
    #return render(request,'blog/test.html',{'articles':serializer.data})
    return Response(serializer.data)
   
@api_view(['GET'])
def articlesApi(request):
    articles = Articles.objects.all()
    serializer = ArticlesListSerializer(articles,many=True)
    #return Response({'articles': reverse('articles',request=request)})
    #return Response({"data":serializer.data,'urls':[reverse('articles',request=request),reverse('articles',request=request),reverse('articles',request=request)]})
    return render(request,'blog/articles_serialized.html',{'articles':serializer.data})
    











