from django.urls import path
from . import views

urlpatterns = [
    path('inscription/', views.inscription, name='inscription'),
    path('insertEvent/', views.event, name='insertEvent'),
    path('acceuil/', views.home, name='acceuil')
]