from django.shortcuts import render, get_object_or_404
from .models import Trip

def home(request):
    trips = Trip.objects
    return render(request, 'trips/home.html', {'trips':trips})

def about(request):
    return render(request, 'about/about.html')

def trip_detail(request, trip_id):
    detail_trip = get_object_or_404(Trip, pk=trip_id)
    return render(request, 'trips/trip_detail.html', {'trip': detail_trip})
