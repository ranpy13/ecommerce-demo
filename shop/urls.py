from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
app_name = 'shop'
urlpatterns = [
    path('', views.all_Clothe, name='clothe'),
    path('add', views.Add_Product, name='Add_Product'),
    path('<str:slug>', views.clothe_Detail, name='product_detail'),



]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
