import random
from django.shortcuts import render
from django.views.generic import ListView
from .models import Post, Category, SocialMedias, Web, Suscriptor


class Inicio(ListView):
    
      def get(self,request,*args,**kwargs):
          return render(request, 'index.html')