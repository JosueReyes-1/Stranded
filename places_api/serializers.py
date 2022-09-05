
from itertools import count
from rest_framework import serializers

from .models import Category, FavoritePlaces, ImgPlace, Place
import json

class CategorySerializerModel(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class ImgPlaceSerializerModel(serializers.ModelSerializer):
    class Meta:
        model = ImgPlace
        fields = ['img']

class FavoritePlaceSerializarModel(serializers.ModelSerializer):
    class Meta:
        model = FavoritePlaces
        fields= ['status']

class PlaceSerializerModel(serializers.ModelSerializer):
    category=CategorySerializerModel()
    images=ImgPlaceSerializerModel(many=True)
    fav=FavoritePlaces.objects.all().count()
    json.dumps(fav)

    class Meta:
        model= Place
        fields = ('name','description','category','country','state','city','images','fav')
