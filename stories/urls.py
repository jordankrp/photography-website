from django.urls import path
from . import views

urlpatterns = [
    path('', views.allstories, name='allstories'),
    path('<int:story_id>/', views.detail, name='detail'),
]
