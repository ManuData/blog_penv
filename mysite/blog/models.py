from unicodedata import category
from unittest.util import _MAX_LENGTH
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from django.contrib.postgres.fields import ArrayField


# Create your models here.

# Metadata Articles

class Articles(models.Model):
    STATUS_CHOICES = (
        ('draft','Draft'),
        ('published','Published'),
    )
    # Datos sobre el articulo
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250,unique_for_date='published')
    body = models.TextField()
    published=models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10,choices=STATUS_CHOICES,default='draft')
    article_description = models.CharField(max_length=350)
    tags = ArrayField(models.CharField(max_length=200), blank=True)
    article_category = models.CharField(max_length=250)
    image_article_list = models.ImageField(upload_to='featured_image')
    #Number of caracters

    def get_absolute_url(self): # 'test' es el nombre de la url dentro del proyecto API
        return reverse('article-detail',kwargs={"slug":self.slug,"pk":self.pk})
    
    def __str__(self):
        return self.title   

    ''' Note: For custom properties
    @property # Custom function that I can retrieve
    def length_tags(self):
        return self.tags[0]
        '''


class Image(models.Model):
    article = models.ForeignKey(Articles,related_name='images',on_delete=models.CASCADE)   
    image = models.ImageField(upload_to='featured_image')


class ManualPDF(models.Model):
    article = models.ForeignKey(Articles,related_name = 'pdfs',on_delete=models.CASCADE)
    pdf = models.FileField(upload_to='pdf')



# Post model para AJAX

class Post (models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()

    def __str__(self):
        return self.title
    
