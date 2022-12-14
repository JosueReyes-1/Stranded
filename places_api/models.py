

from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name=models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Place(models.Model):
    name=models.CharField(max_length=50)
    description=models.CharField(max_length=100)
    category=models.ForeignKey(Category,on_delete=models.CASCADE,null=True)
    latitude=models.CharField(max_length=50,null=True)
    longitude=models.CharField(max_length=50,null=True)
    country=models.CharField(max_length=30) 
    state=models.CharField(max_length=20)
    city=models.CharField(max_length=20)
    address=models.CharField(max_length=60,null=True)

class ImgPlace(models.Model):

    img=models.CharField(max_length=200)
    place=models.ForeignKey(Place,related_name='images',on_delete=models.CASCADE)

    def __str__(self):
        return self.img

class FavoritePlaces(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    place=models.ForeignKey(Place,related_name='place',on_delete=models.CASCADE)
    status=models.BooleanField(default=True)
