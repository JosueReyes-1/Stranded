from rest_framework.views import APIView
from django.db.models import Q
from django.http import JsonResponse
from .models import Place, ImgPlace
# Place.objects.filter(city=city,state=state,country=country) | | Place.objects.filter(country=country)
def validateData(country=None, state=None, city=None, category=None):
        if (country and state and city):
            if (country and state and city and category):
                return Place.objects.filter(city=city, state=state, country=country, category__name=category)
            else:
                return Place.objects.filter(city=city, state=state, country=country)
        elif (country and state):
            if (country and state and category):
                return Place.objects.filter(country=country, state=state, category__name=category)
            else:
                return Place.objects.filter(country=country, state=state)
        elif (country):
            if (country and category):
                return Place.objects.filter(country=country, category__name=category)
            else:
                return Place.objects.filter(country=country)
        

class PlaceAPiView(APIView):
    def get(self, request, country=None, state=None, city=None, category=None, format=None):
        consulta=validateData(country, state, city, category)
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
