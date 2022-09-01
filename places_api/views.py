from rest_framework.views import APIView

from django.http import JsonResponse
from .models import Place,ImgPlace

class PlaceAPiView(APIView):
    def get(self,request,country=0,city=0,state=0,format=None):
        

        

        consulta=Place.objects.filter(city=city,state=state,country=country) | Place.objects.filter(state=state,country=country) | Place.objects.filter(country=country) 
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
