from django.shortcuts import render
from .models import Country, City


def get_countries(request):
    countries = Country.objects.all()
    return render(request, 'countries.html', {'countries': countries})