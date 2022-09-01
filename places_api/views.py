from email.mime import image
from json import JSONDecoder
from unittest import result
from rest_framework.views import APIView
from rest_framework.response import Response

from django.http import JsonResponse
from .models import Place,ImgPlace

class PlaceAPiView(APIView):
    def get(self,request,locate,format=None):
        consulta=Place.objects.filter(country=locate) | Place.objects.filter(state=locate)
        result1=[]
        for o in consulta:
            imagenes=ImgPlace.objects.filter(place_id=o.pk)
            listaimg=[]
            for i in imagenes:
                listaimg.append([i.img])
            result1.append({
                'name':o.name,
                'descrition':o.description,
                'country':o.country,
                'state':o.state,
                'city':o.city,
                'img':listaimg,
            })
        
        return JsonResponse(
            result1,
            safe=False
        )
