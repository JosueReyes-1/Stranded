from django.urls import path

from places_api import views

urlpatterns = [
    path('place/c=<str:country>',views.PlaceAPiView.as_view()),
    path('place/c=<str:country>/s=<str:state>',views.PlaceAPiView.as_view()),
    path('place/c=<str:country>/s=<str:state>/ci=<str:city>',views.PlaceAPiView.as_view()),

    path('place/c=<str:country>/cg=<str:category>',views.PlaceAPiView.as_view()),
    path('place/c=<str:country>/s=<str:state>/cg=<str:category>',views.PlaceAPiView.as_view()),
    path('place/c=<str:country>/s=<str:state>/ci=<str:city>/cg=<str:category>',views.PlaceAPiView.as_view()),
]