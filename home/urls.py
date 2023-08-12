from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
app_name='home'
urlpatterns = [
    path('', views.home,name='home'),
      path('h', views.home1,name='home1'),
   
    
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
