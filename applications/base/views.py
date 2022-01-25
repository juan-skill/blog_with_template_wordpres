from multiprocessing import context
import random
from turtle import pos
from django.shortcuts import render
from django.views.generic import ListView
from .models import Post, Category, SocialMedias, Web, Suscriptor


class Inicio(ListView):
    
    def get(self,request,*args,**kwargs):
        posts = list(Post.objects.filter(
                status = True,
                published = True
                ).values_list('id', flat = True))
        print(posts)
        
        main_post = random.choice(posts)
        
        main_post = Post.objects.get(id = main_post)
        
        print(main_post)
        
        context = {
            'main':  main_post,
        }        
        
        return render(request, 'index.html', context)