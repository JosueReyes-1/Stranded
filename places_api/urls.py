
from django.urls import path

from places_api import views

urlpatterns = [
    path('place/',views.SearchApiView.as_view()),

]