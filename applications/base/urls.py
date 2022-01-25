from django.urls import path
from .views import Inicio, Listado

urlpatterns = [
    path('', Inicio.as_view(), name = 'index'),
    path('videojuegos/',Listado.as_view(), name = 'videogames'),
]
