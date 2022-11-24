from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('<int:trip_id>/', views.trip_detail, name='trip_detail'),
]
