from django.shortcuts import render
from .models import Trip

def home(request):
    trips = Trip.objects
    return render(request, 'trips/home.html', {'trips':trips})
