from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
app_name='shop'
urlpatterns = [
    path('signup', views.signup,name='signup'),
    path('profile', views.profile,name='profile'),
    path('profile/edit', views.profile_edit,name='profile_edit'),
    
    
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
