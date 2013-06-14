from django.db import models
from django.forms import ModelForm

# Create your models here.
class Article(models.Model):
     title = models.CharField(max_length = 120, unique = True)
     slug  = models.SlugField(max_length = 120, unique = True)
     date_published = models.DateTimeField(auto_now=True)
     body = models.TextField()
     images = models.URLField()
     
     def __str__(self):
        return self.title
     

class Comment(models.Model):     
     username = models.CharField(max_length = 120, unique = True)
     display_name = models.CharField(max_length = 120, unique = True)
     comment = models.TextField()
     date_published = models.DateTimeField(auto_now = True)
     user_image = models.URLField()
     article = models.ForeignKey('Article') 

     def __str__(self):
        return self.username
