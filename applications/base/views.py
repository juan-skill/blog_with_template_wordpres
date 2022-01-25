import random
from turtle import pos
from django.shortcuts import render
from django.views.generic import ListView
from django.core.paginator import Paginator
from .models import Post, Category, SocialMedias, Web, Suscriptor


def getPostbyId(id):
    try: 
        return Post.objects.get(id = id)
    except:
        return None
    
def getSocialNetwork():
    return SocialMedias.objects.filter(status = True).latest('date_created')

def getWeb():
    return Web.objects.filter(status = True).latest('date_created')
    

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
    
    
class Listado(ListView):

    def get(self, request, *args,**kwargs):
        posts = Post.objects.filter(
                status = True,
                published = True,
                category = Category.objects.get(name = 'Video Games')
                )
        try:
            category = Category.objects.get(name = 'Video Games')
        except:
            category = None

        
        paginator = Paginator(posts,3)
        pagina = request.GET.get('page')
        posts = paginator.get_page(pagina)
        

        context = {
            'posts':posts,
            'socials': getSocialNetwork(),
            'web': getWeb(),
            'category': category,
        }
        
        return render(request,'category.html', context)
    

class GeneralList(ListView):

    def get(self, request, *args,**kwargs):
        posts = Post.objects.filter(
                status = True,
                published = True,
                category = Category.objects.get(name = 'General')
                )
        try:
            category = Category.objects.get(name = 'General')
        except:
            category = None

        
        paginator = Paginator(posts,3)
        pagina = request.GET.get('page')
        posts = paginator.get_page(pagina)
        

        context = {
            'posts':posts,
            'socials': getSocialNetwork(),
            'web': getWeb(),
            'category': category,
        }
        
        return render(request,'category.html', context)    