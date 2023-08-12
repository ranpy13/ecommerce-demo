from django.shortcuts import render ,redirect
from django.urls import reverse
from shop.models import clothe
from .models import blog
from django.core.paginator import Paginator
from .forms import ReviewForm,BlogForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def all_Blogs(request):

    blog_list=blog.objects.all()
    clothe_list1 = clothe.objects.first()
    clothe_list2 = clothe.objects.last()
    clothe_list3 = clothe.objects.get(id=2)
    paginator = Paginator(blog_list, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    contxt={'blogs':page_obj,'clothe': clothe_list1,'clothe2': clothe_list2,'clothe3': clothe_list3}
    return render(request,"blog/blog_list.html",contxt)
    
def blog_Detail(request,slug):
    blog_d=blog.objects.get(slug=slug)
    clothe_list1 = clothe.objects.first()
    clothe_list2 = clothe.objects.last()
    clothe_list3 = clothe.objects.get(id=2)
    
    if request.method=='POST':
         form= ReviewForm(request.POST)
         if form.is_valid:
             myform=form.save(commit=False)
             myform.blog_r=blog_d
             myform.save()
    else:
        form= ReviewForm()
    contxt={'detail':blog_d,'form':form,'clothe': clothe_list1,'clothe2': clothe_list2,'clothe3': clothe_list3}
    return render(request,"blog/blog_detail.html",contxt)




@login_required
def Add_Blog(request):

    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid:
            myform = form.save(commit=False)
            myform.owner = request.user
            myform.save()
            return redirect(reverse('blog:blog'))
    else:
        form = BlogForm()
    return render(request, 'blog/add_blog.html', {"form": form})


def Featured_Products(request):

    clothe_list1 = clothe.objects.first()
    clothe_list2 = clothe.objects.last()
    clothe_list3 = clothe.objects.get(id=2)
    
    contxt = {'clothe': clothe_list1,'clothe2': clothe_list2,'clothe3': clothe_list3}
    return render(request,"blog/blog_detail.html",contxt)
