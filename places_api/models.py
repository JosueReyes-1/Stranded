from doctest import debug_script
from unicodedata import category
from django.db import models

# Create your models here.
class Category(models.Model):
    category=models.CharField(max_length=50)

class Place(models.Model):
    name=models.CharField(max_length=50)
    description=models.CharField(max_length=100)
    category=models.ForeignKey(Category,on_delete=models.CASCADE,null=True)
    country=models.CharField(max_length=30) 
    state=models.CharField(max_length=20)
    city=models.CharField(max_length=20)

class ImgPlace(models.Model):
    img=models.CharField(max_length=200)
    place=models.ForeignKey(Place,on_delete=models.CASCADE)