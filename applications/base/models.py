from django.db import models
from ckeditor.fields import RichTextField

class ModeloBase(models.Model):
    
    id = models.AutoField(primary_key = True)
    status = models.BooleanField('Status',default = True)
    date_created = models.DateField('Date created',auto_now = False, auto_now_add = True)
    date_of_change = models.DateField('Date modified',auto_now = True, auto_now_add = False)
    date_deleted = models.DateField('Date eliminated ',auto_now = True, auto_now_add = False)

    class Meta:
        abstract = True
        
        
class Category(ModeloBase):
    
    name = models.CharField('Name of Category', max_length = 100, unique = True)
    image_referencial = models.ImageField('Image Referencial',upload_to = 'categoria/')

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.nombre
    

class Author(ModeloBase):
    
    name = models.CharField('Names',max_length = 100)
    last_name = models.CharField('Last name',max_length = 120)
    email = models.EmailField('Email', max_length = 200)
    description = models.TextField('Description')
    image_referencial = models.ImageField('Image Referencial', null = True, blank = True,upload_to = 'autores/')
    web = models.URLField('Web', null = True, blank = True)
    facebook = models.URLField('Facebook', null = True, blank = True)
    twitter = models.URLField('Twitter', null = True, blank = True)
    instagram = models.URLField('Instagram', null = True, blank = True)

    class Meta:
        verbose_name = 'Author'
        verbose_name_plural = 'Authors'

    def __str__(self):
        return f'{self.last_name},{self.name}'


class Post(ModeloBase):
    
    title = models.CharField('Title of post',max_length = 150, unique = True)
    slug = models.CharField('Slug', max_length = 150, unique = True)
    description = models.TextField('Description')
    author = models.ForeignKey(Author, on_delete = models.CASCADE)
    category = models.ForeignKey(Category, on_delete = models.CASCADE)
    content = RichTextField()
    image_referencial = models.ImageField('Referencial Image', upload_to = 'imagenes/', max_length = 255)
    published = models.BooleanField('Publish / No Publish',default = False)
    date_published = models.DateField('Date of publish')

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'

    def __str__(self):
        return self.title
    
    
class Web(ModeloBase):
    
    contact_us = models.TextField('Contact us')
    phone_number = models.CharField('Phone number', max_length = 10)
    email = models.EmailField('Email', max_length = 200)
    address = models.CharField('Address', max_length = 200)

    class Meta:
        verbose_name = 'Web'
        verbose_name_plural = 'Webs'

    def __str__(self):
        return self.contact_us
    

class SocialMedias(ModeloBase):
    
    facebook = models.URLField('Facebook')
    twitter = models.URLField('Twitter')
    instagram = models.URLField('Instagram')

    class Meta:
        verbose_name = 'Social media'
        verbose_name_plural = 'Social medias'

    def __str__(self):
        return self.facebook
    

class Contact(ModeloBase):
    
    name = models.CharField('Name', max_length = 100)
    last_name = models.CharField('Last name', max_length = 150)
    email = models.EmailField('Email', max_length = 200)
    subject = models.CharField('Subject', max_length = 100)
    message = models.TextField('Message')

    class Meta:
        verbose_name = 'Contact'
        verbose_name_plural = 'Contacts'

    def __str__(self):
        return self.subject
    
    
class Suscriptor(ModeloBase):
    
    email = models.EmailField('Email', max_length = 200)

    class Meta:
        verbose_name = 'Suscriptor'
        verbose_name_plural = 'Suscriptors'

    def __str__(self):
        return self.email
