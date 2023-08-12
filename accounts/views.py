from django.shortcuts import redirect, render
from django.urls import reverse
from .forms import SignupForm ,ProfileForm,UserForm
from django.contrib.auth import authenticate , login
from .models import Profile
# Create your views here.
def signup(request):
    if request.method=="POST":
        form=SignupForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data['username']
            password=form.cleaned_data['password']
            user=authenticate(username=username,password=password)
            login(request,user)
            return redirect(reverse('accounts:profile'))

    else:
       form=SignupForm()
    return render(request,'registration/signup.html',{'form':form}) 

    

def profile(request):
     profile=Profile.objects.get(user=request.user)
     return render(request,'accounts/profile.html',{"profile":profile})

def profile_edit(request):
    profile=Profile.objects.get(user=request.user)
    if request.method=='POST':
        userform=UserForm(request.POST,request.FILES,instance=request.user)
        profileform=ProfileForm(request.POST,request.FILES,instance=profile)
        if userform.is_valid() and profileform.is_valid():
            userform.save()
            myprofile=profileform.save(commit=False)
            myprofile.user=request.user
            myprofile.save()
            return redirect(reverse('accounts:profile'))

    else:
        userform=UserForm(instance=request.user)
        profileform=ProfileForm(instance=profile)
        contxt={'userform':userform,'profileform':profileform}
    return render(request,'accounts/profile_edit.html',contxt)