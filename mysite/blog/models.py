from unicodedata import category
from django.db import models



# Create your models here.

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

class Articles(models.Model):

    # Datos sobre el articulo
    title = models.CharField(max_length=100)
    article_category = models.CharField(max_length=100)
    pub_date = models.DateTimeField('date published')
    date = models.DateTimeField(auto_now_add = True)
    body = models.CharField(max_length=1500)
    # Es la url del artículo separada por guiones | "hyphen" (-)
    slug = models.SlugField()
    
    

    def __str__(self):
        return self.title


