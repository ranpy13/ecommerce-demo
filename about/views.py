from django.shortcuts import render

# Create your views here.
def about(reqist):

    return render(reqist,'about/about.html',{'x':0})