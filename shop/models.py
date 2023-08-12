from unicodedata import name
from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User
from django.utils.html import format_html

# Create your models here.
size_type = (('S', 'S'),
             ('M', "M"),
             ("L", "L"),
             ('XL', 'XL'),
             ('2XL', '2XL'))


Materials_type = (('Chiffon', 'Chiffon'),
             ('Cotton', "Cotton"),
             ("Crepe", "Crepe"),
             ('Denim', 'Denim'),
             ('Lace', 'Lace'),
             ('Leather', 'Leather'),
             ('Linen', 'Linen'),
             ('Satin', 'Satin'),
             ('Silk', 'Silk'),
             ('Synthetics', 'Synthetics'),
             ('Wool', 'Wool'),
             )


def upload_img(instace,filename):
    imgname,ext=filename.split('.')

    return f"clothes/{instace.slug}.{ext}"
class Size(models.Model):

    name = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.name

class Color(models.Model):
    code = models.CharField(max_length=20, unique=True)
    name=models.CharField(max_length=20)

    def __str__(self):
        # return format_html('<div style="background-color: {fcode};width:100px;height:100px"></div>'.format(fcode=self.code))
        return self.name 

class clothe(models.Model):
    owner=models.ForeignKey(User, related_name='pro_owner', on_delete=models.CASCADE)
    title = models.CharField(max_length=25)
    price = models.FloatField(max_length=5)
    Brief_summary = models.CharField(max_length=200)
    sizes = models.ManyToManyField(Size)
    colors = models.ManyToManyField(Color)
    #color
    descripion=models.TextField(max_length=800)
    Weight=models.FloatField(max_length=4)
    Dimensions=models.CharField(max_length=18)
    Materials_name=models.CharField(max_length=20,choices=Materials_type)
    Materials=models.FloatField(max_length=2)
    puplish_at=models.DateField(auto_now=True)
    category=models.ForeignKey('Category',on_delete= models.CASCADE)
    image=models.ImageField(upload_to=upload_img)
    image2=models.ImageField(upload_to=upload_img)
    image3=models.ImageField(upload_to=upload_img)
    slug=models.SlugField(blank=True,null=True)

    def save(self,*args,**kwargs):
        self.slug=slugify(self.title) 
        super(clothe,self).save(*args,**kwargs)
    
    def __str__(self) :
        return self.title
        


class Category(models.Model):
        name=models.CharField(max_length=25)

        def __str__(self):
            return self.name


class review(models.Model):
    
    clothe_r=models.ForeignKey(clothe,related_name='add_review', on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)
    Your_review=models.TextField(max_length=700)
    creat_at=models.DateField(auto_now=True)
    def __str__(self) :
        return self.name