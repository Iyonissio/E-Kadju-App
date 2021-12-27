

from django import contrib
from django import urls
from django.contrib import admin
from django.urls import path  , include
from django.conf import settings
from django.conf.urls.static import static

from .import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('master/', views.Master, name='master'),
    path('', views.Index, name='index'),
    
    path('signup', views.signup, name='signup'),
    path('accounts/', include('django.contrib.auth.urls')),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
