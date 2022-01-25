from django.core.paginator import Paginator
from .models import Post, Category, SocialMedias, Web

def getPostbyId(id):
    try: 
        return Post.objects.get(id = id)
    except:
        return None
    
def getSocialNetwork():
    return SocialMedias.objects.filter(status = True).latest('date_created')

def getWeb():
    return Web.objects.filter(status = True).latest('date_created')


def generate_category(request, category_name):
    posts = Post.objects.filter(
            status = True,
            published = True,
            category = Category.objects.get(name = category_name)
            )
    try:
        category = Category.objects.get(name = category_name)
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
    return context