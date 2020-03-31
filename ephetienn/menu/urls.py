from . import views
from django.urls import path


urlpatterns = [
    path('inscription/', views.inscription, name='inscription'),
    path('insertEvent/', views.event, name='insertEvent'),
    path('supEvent/', views.supEvent, name='supEvent'),
    path('acceuil/', views.home, name='acceuil'),
    path('contact/', views.emailView, name='contact'),
    path('success/', views.successView, name='success'),
    path('admin/', views.admin, name='admin'),
    path('membre/', views.affMembre, name='membre'),
    path('modifierMembre/', views.modifMembre, name="modifierMembre"),
    path('modifierMembre/', views.affMembre, name="modifierMembre"),
    path('supMembre/', views.supMembre, name='supMembre'),
    path('affEvent/', views.affEvent, name='affEvent'),


]
