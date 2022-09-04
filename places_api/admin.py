from django.contrib import admin
from .models import FavoritePlaces, Place,ImgPlace,Category
# Register your models here.

class ImagenPlaces (admin.TabularInline):
    model=ImgPlace

class PlacesAdmin(admin.ModelAdmin):
    list_display=["name","description","country","state","city"]
    inlines=[
        ImagenPlaces
    ]

admin.site.register(Place,PlacesAdmin)
admin.site.register(Category)
admin.site.register(FavoritePlaces)