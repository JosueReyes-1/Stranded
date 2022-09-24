from django.http import JsonResponse
from places_api.serializers import PlaceSerializerModel
from .models import Place,ImgPlace
from rest_framework.filters import SearchFilter,OrderingFilter
from rest_framework.generics import ListAPIView

from django_filters.rest_framework import DjangoFilterBackend
from django.db.models import Count
class SearchApiView(ListAPIView):
    
    queryset=Place.objects.all()
    serializer_class=PlaceSerializerModel
    filter_backends=(SearchFilter,OrderingFilter,DjangoFilterBackend)
    search_fields=('name','category__name')
    filterset_fields=['country','state','city']

