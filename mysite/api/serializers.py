from rest_framework import serializers
from blog.models import Articles,Image
from rest_framework.reverse import reverse




class ArticlesSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Articles
        fields = '__all__'


''' Me devuelve los objetos en formato de string
class ArticlesListSerializer(serializers.ModelSerializer):
    url = serializers.CharField(source='get_absolute_url', read_only=True)
    images = serializers.StringRelatedField(many=True)

    class Meta: 
        model = Articles
        fields = [
            'url',
            'title',
            'published',
            'article_description',
            'image_article_list',
            'images'
            ]

'''


class ImageSerializer(serializers.ModelSerializer):

    class Meta: 
        model = Image
        fields = '__all__'

    

class ArticlesListSerializer(serializers.ModelSerializer):
    url = serializers.CharField(source='get_absolute_url', read_only=True)
    images = ImageSerializer(many=True, read_only=True)

    class Meta: 
        model = Articles
        fields = [
            'url',
            'title',
            'published',
            'article_description',
            'body',
            'image_article_list',
            'images',
            'id',
            'tags',
            ]
        

    
  