from django.contrib import admin
from .models import Place,ImgPlace
# Register your models here.

class ImagenPlaces (admin.TabularInline):
    model=ImgPlace

class PlacesAdmin(admin.ModelAdmin):
    list_display=["name","description","country","state","city"]
    inlines=[
        ImagenPlaces
    ]

admin.site.register(Place,PlacesAdmin)