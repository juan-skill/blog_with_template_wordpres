from multiprocessing import context
import random
from turtle import pos
from django.shortcuts import render
from django.views.generic import ListView
from .models import Post, Category, SocialMedias, Web, Suscriptor


def getPostbyId(id):
    return Post.objects.get(id = id)

class Inicio(ListView):
    
    def get(self,request,*args,**kwargs):
        posts = list(Post.objects.filter(
                status = True,
                published = True
                ).values_list('id', flat = True))
        print(posts)
        
        main_post = random.choice(posts)
        
        main_post = getPostbyId(main_post)
        
        post1 = random.choice(posts)
        posts.remove(post1)
        post2 = random.choice(posts)
        posts.remove(post2)
        post3 = random.choice(posts)
        posts.remove(post3)
        post4 = random.choice(posts)
        posts.remove(post4)
        
        print(main_post)
        
        context = {
            'main':  main_post,
            'post1': getPostbyId(post1),
            'post2': getPostbyId(post2),
            'post3': getPostbyId(post3),
            'post4': getPostbyId(post4),
        }        
        
        return render(request, 'index.html', context)