from django.urls import path
from .views import Inicio, Listed, FormContact, DetailPost

urlpatterns = [
    path('', Inicio.as_view(), name = 'index'),
    path('videojuegos/',Listed.as_view(), {'category_name': 'Video Games'}, name = 'videogames'),
    path('generales/', Listed.as_view(), { 'category_name': 'General'},name = 'generales'),
    path('formulario_contacto/', FormContact.as_view(), name = 'formcontact'),
    path('<slug:slug>/',DetailPost.as_view(), name = 'detalle_post'),
]
