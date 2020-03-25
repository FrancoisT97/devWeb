from . import views
from django.urls import path

from .views import emailView, successView

urlpatterns = [
    path('inscription/', views.inscription, name='inscription'),
    path('insertEvent/', views.event, name='insertEvent'),
    path('acceuil/', views.home, name='acceuil'),
    path('contact/', emailView, name='contact'),
    path('success/', successView, name='success'),

]
