from django.urls import path
from .views import Inicio, Listed

urlpatterns = [
    path('', Inicio.as_view(), name = 'index'),
    path('videojuegos/',Listed.as_view(), {'category_name': 'Video Games'}, name = 'videogames'),
    path('generales/', Listed.as_view(), { 'category_name': 'General'},name = 'generales'),
]
