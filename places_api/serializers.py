

from rest_framework import serializers

from .models import Category, FavoritePlaces, ImgPlace, Place


class CategorySerializerModel(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class ImgPlaceSerializerModel(serializers.ModelSerializer):
    class Meta:
        model = ImgPlace
        fields = ['img']

class PlaceSerializerModel(serializers.ModelSerializer):
    category=CategorySerializerModel()
    images=ImgPlaceSerializerModel(many=True)
    
    class Meta:
        model= Place
        fields = ('name','description','category','country','state','city','address','latitude','longitude','images')



class FavoritePlaceSerializarModel(serializers.ModelSerializer):
    place = PlaceSerializerModel()
 
    class Meta:
        model = FavoritePlaces
        fields= 'place'