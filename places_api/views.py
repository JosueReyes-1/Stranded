from rest_framework import generics
from django.db.models import Q
from django.http import JsonResponse
from places_api.additionalFunctions import QueryData
from places_api.serializers import PlaceSerializerModel
from .models import Place,ImgPlace

from rest_framework.filters import SearchFilter,OrderingFilter
from rest_framework.generics import ListAPIView

class PlaceAPiView(ListAPIView): 
    def get(self, request, country=None, state=None, city=None, category=None, format=None):
        consulta=QueryData(country, state, city, category)
        result1 = []
        for o in consulta:
            imagenes = ImgPlace.objects.filter(place_id=o.pk)
            listaimg = []
            for i in imagenes:
                listaimg.append([i.img])
            result1.append({
                'name': o.name,
                'descrition': o.description,
                'country': o.country,
                'state': o.state,
                'city': o.city,
                'category': o.category.name,
                'img': listaimg,
            })
        return JsonResponse(result1,safe=False)

class SearchApiView(ListAPIView):
    queryset=Place.objects.all()
    serializer_class=PlaceSerializerModel
    filter_backends=(SearchFilter,OrderingFilter)
    search_fields=('name','category__name')