
from rest_framework import serializers

from .models import Place





class PlaceSerializerModel(serializers.ModelSerializer):
    images=serializers.StringRelatedField(many=True)
    category=serializers.CharField(source='category.name')
    class Meta:
        model= Place
        fields = ('name','description','category','country','state','city','images')

