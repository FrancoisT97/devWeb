from django.urls import path
from . import views

urlpatterns = [
    path('acceuil', views.home),
]