from django.urls import path

from places_api import views

urlpatterns = [
    path('place/c=<str:locate>',views.PlaceAPiView.as_view()),     
]