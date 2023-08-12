from django.http import JsonResponse
from django.urls import reverse
from django.shortcuts import redirect, render
from .models import clothe
from .forms import ReviewForm, ClotheForm
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from .filters import ProductFilter

# Create your views here.


def all_Clothe(request):

    clothe_list = clothe.objects.all()
    myfilter=ProductFilter(request.GET,queryset=clothe_list)
    clothe_list=myfilter.qs
    paginator = Paginator(clothe_list, 2)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    contxt = {'clothes': clothe_list, 'myfilter':myfilter}
    return render(request, "clothe/product_list.html", contxt)


def clothe_Detail(request, slug):
    clothe_d = clothe.objects.get(slug=slug)
    clothe_list = clothe.objects.all()
    
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form .is_valid:
            myform = form.save(commit=False)
            myform.clothe_r = clothe_d
            myform.save()
    else:
        form = ReviewForm()
    contxt = {'detail': clothe_d, 'clotes': clothe_list, 'form': form}
    return render(request, "clothe/product_detail.html", contxt)

@login_required
def Add_Product(request):

    if request.method == 'POST':
        form = ClotheForm(request.POST, request.FILES)
        if form .is_valid:
            myform = form.save(commit=False)
            myform.owner = request.user
            myform.save()
            return redirect(reverse('clothe:clothe'))
    else:
        form = ClotheForm()
    return render(request, 'clothe/add_product.html', {"form": form})
