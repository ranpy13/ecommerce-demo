from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
app_name='contact'
urlpatterns = [
    path('', views.contact1,name='contact'),
   
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
