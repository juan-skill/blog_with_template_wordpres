import random
from django.shortcuts import render, redirect
from django.views.generic import ListView, View, DetailView
from .forms import ContactForm
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


class FormContact(View):
    def get(self,request,*args,**kwargs):
        
        form = ContactForm()
        context = {
            'socials': getSocialNetwork(),
            'web': getWeb(),
            'form': form,    
        }
        
        return render(request, 'contact.html', context)    
    
    def post(self,request,*args,**kwargs):
        form = ContactForm(request.POST)
        
        if form.is_valid():
            form.save()
            return redirect('base:index')
        else:
            context = {
                'form':form,
            }
            return render(request,'contact.html', context)


class DetailPost(DetailView):
    
    def get(self,request,slug,*args,**kwargs):
        try:
            post = Post.objects.get(slug = slug)
        except:
            post = None
        
        posts = list(Post.objects.filter(
                status = True,
                published = True
                ).values_list('id',flat = True))
        
        """
        posts.remove(post.id)
        post1 = random.choice(posts)
        posts.remove(post1)
        post2 = random.choice(posts)
        posts.remove(post2)
        post3 = random.choice(posts)
        posts.remove(post3)
        """

        context = {
            'post':post,
            'socials':getSocialNetwork(),
            'web':getWeb(),
            #'post1':getPostbyId(post1),
            # 'post2':getPostbyId(post2),
            #'post3':getPostbyId(post3),
        }
        
        return render(request, 'post.html', context)