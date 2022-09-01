from django.db import models

# Create your models here.

class Place(models.Model):
    name=models.CharField(max_length=50)
    description=models.CharField(max_length=100)
    country=models.CharField(max_length=30) 
    state=models.CharField(max_length=20)
    city=models.CharField(max_length=20)

class ImgPlace(models.Model):
    img=models.CharField(max_length=200)
    place=models.ForeignKey(Place,on_delete=models.CASCADE)