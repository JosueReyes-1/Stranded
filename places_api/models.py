from doctest import debug_script
from unicodedata import category, name
from django.db import models

# Create your models here.
class Category(models.Model):
    name=models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Place(models.Model):
    name=models.CharField(max_length=50)
    description=models.CharField(max_length=100)
    category=models.ForeignKey(Category,on_delete=models.CASCADE,null=True)
    country=models.CharField(max_length=30) 
    state=models.CharField(max_length=20)
    city=models.CharField(max_length=20)

class ImgPlace(models.Model):
    img=models.CharField(max_length=200)
    place=models.ForeignKey(Place,related_name='images',on_delete=models.CASCADE)

    def __str__(self):
        return self.img