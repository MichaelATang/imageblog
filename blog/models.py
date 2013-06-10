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
     

