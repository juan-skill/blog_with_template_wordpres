from django.urls import path
from .views import Inicio, Listado, GeneralList

urlpatterns = [
    path('', Inicio.as_view(), name = 'index'),
    path('videojuegos/',Listado.as_view(), name = 'videogames'),
    path('generales/', GeneralList.as_view(), name = 'generales'),
]
