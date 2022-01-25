import random
from django.shortcuts import render
from django.views.generic import ListView
from .models import Post, Category, SocialMedias, Web, Suscriptor
from .utils import *


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
        
        try:
            post_videogames = Post.objects.filter(
                                status = True,
                                published = True,
                                category = Category.objects.get(name = 'Video Games')
                                ).latest('date_published')
        except:
            post_videogames = None

        try:
            post_general = Post.objects.filter(
                            status = True,
                            published = True,
                            category = Category.objects.get(name = 'General')
                            ).latest('date_published')
        except:
            post_general = None
        
        context = {
            'main':  main_post,
            'post1': getPostbyId(post1),
            'post2': getPostbyId(post2),
            'post3': getPostbyId(post3),
            'post4': getPostbyId(post4),
            'post_general':post_general,
            'post_videogames':post_videogames,
            'socials':getSocialNetwork(),
            'web':getWeb(),            
        }        
        
        return render(request, 'index.html', context)
    

class Listed(ListView):

    def get(self,request, category_name, *args,**kwargs):
        context = generate_category(request, category_name)
        return render(request,'category.html', context)  