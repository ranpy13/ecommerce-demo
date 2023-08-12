from django.shortcuts import render


# Create your views here.

def home(requist):

    return render(requist,'home/index.html',{'x':0})

def home1(requist):

    return render(requist,'home/index2.html',{'x':0})