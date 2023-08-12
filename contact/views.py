from django.conf import settings
from django.shortcuts import render
from .models import Info
from django.core.mail import send_mail

# Create your views here.
def contact1(request):
   
    myInfo=Info.objects.first()

    if request.method=='POST':
        email=request.POST['email']
        message=request.POST['msg']
        Subject=request.POST['Subject']
        send_mail(
                
                Subject ,
        
                message,
                email,
                [settings.EMAIL_HOST_USER],
                # fail_silently=False,
                
         )

       

    return render(request,"contact/contact.html",{"myInfo":myInfo})