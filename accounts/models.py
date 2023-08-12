from distutils.command.upload import upload
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.
class Profile(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    city=models.ForeignKey("City", related_name='user_city', on_delete=models.CASCADE ,null=True,blank=True)
    phone_number=models.CharField(max_length=15)
    profile_image=models.ImageField(upload_to='profile/',null=True,blank=True)
    def __str__(self) :
        return str(self.user)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


class City(models.Model):
    city=models.CharField(max_length=30)
    def __str__(self) :
        return self.city