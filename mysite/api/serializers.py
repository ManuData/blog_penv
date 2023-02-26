from rest_framework import serializers
from blog.models import Articles,Image
from rest_framework.reverse import reverse




class ArticlesSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Articles
        fields = '__all__'

class ArticlesListSerializer(serializers.ModelSerializer):
    url = serializers.CharField(source='get_absolute_url', read_only=True)
    class Meta: 
        model = Articles
        fields = [
            'url',
            'title',
            'published',
            'article_description',
            'image_article_list',
            ]

    
  


