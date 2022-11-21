from django.shortcuts import render, get_object_or_404
from .models import Story

def allstories(request):
    stories = Story.objects
    return render(request, 'stories/allstories.html', {'stories':stories})

def detail(request, story_id):
    detail_story = get_object_or_404(Story, pk=story_id)
    return render(request, 'stories/detail.html', {'story': detail_story})
