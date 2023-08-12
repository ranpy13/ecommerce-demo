from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User

# Create your models here.

def upload_img(instace,filename):
    imgname,ext=filename.split('.')

    return f"blogs/{instace.slug}.{ext}"


class blog(models.Model):
        owner=models.ForeignKey(User, related_name='pro_owner2', on_delete=models.CASCADE)
        title = models.CharField(max_length=25)
        Brief_summary = models.CharField(max_length=200)
        descripion=models.TextField(max_length=1000)
        puplish_at=models.DateField(auto_now=True)
        category=models.ForeignKey('Category',on_delete= models.CASCADE)
        image=models.ImageField(upload_to=upload_img)
        slug=models.SlugField(blank=True,null=True)
        def save(self,*args,**kwargs):
            self.slug=slugify(self.title) 
            super(blog,self).save(*args,**kwargs)
    
        def __str__(self) :
          return self.title
        


class Category(models.Model):
        name=models.CharField(max_length=25)

        def __str__(self):
            return self.name


class review(models.Model):
    # owner=models.ForeignKey(User, related_name='pro_owner1', on_delete=models.CASCADE)
    blog_r=models.ForeignKey(blog,related_name='add_review', on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)
    comment=models.TextField(max_length=700)
    creat_at=models.DateField(auto_now=True)
    website=models.URLField()
    def __str__(self) :
        return self.name