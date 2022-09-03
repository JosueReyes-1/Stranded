from .models import Place

def QueryData(country=None, state=None, city=None, category=None):
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
