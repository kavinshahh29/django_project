
from django.conf import settings
import projects
from django.contrib import admin
from django.urls import path,include
from django.http import HttpResponse
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('projectapp/',include('projectapp.urls')),
    path('',include('userapp.urls')),    
]

urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

urlpatterns+=static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)


