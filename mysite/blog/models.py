from unicodedata import category
from unittest.util import _MAX_LENGTH
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse




# Create your models here.

# Metadata Articles

class Articles(models.Model):
    STATUS_CHOICES = (
        ('draft','Draft'),
        ('published','Published'),

    )

    # Datos sobre el articulo
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250,unique_for_date='publish')
    author = models.ForeignKey(User,on_delete=models.CASCADE,related_name='blog_posts')
    body = models.TextField()
    published=models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10,choices=STATUS_CHOICES,default='draft')
    article_description = models.CharField(max_length=350)

    def get_absolute_url(self):
        return reverse('article-detail',kwargs={"slug":self.slug})
    

    def __str__(self):
        return self.title


