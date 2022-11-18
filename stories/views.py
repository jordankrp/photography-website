from django.shortcuts import render
from .models import Story

def allstories(request):
    stories = Story.objects
    return render(request, 'stories/allstories.html', {'stories':stories})
