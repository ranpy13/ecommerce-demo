from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
app_name='blog'
urlpatterns = [
    path('', views.all_Blogs,name='blog'),
    path('add', views.Add_Blog, name='Add_Blog'),
    path('<str:slug>',views.blog_Detail,name='blog_detail'),
    
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
