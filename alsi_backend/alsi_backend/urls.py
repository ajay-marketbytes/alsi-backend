"""
URL configuration for alsi_backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('authapp.urls')),
    path('api/home/', include('home.urls')),
    path('api/layout/', include('layouts.urls')),
    path('api/service/', include('services.urls')),
    path('api/market/', include('market.urls')),
    path('api/social-media/', include('social_media.urls')),
    path('api/images/', include('image_storage.urls')),
    path('api/about/', include('about.urls')),
    path('api/industry/', include('industry.urls')),
    path('api/contact/', include('contact.urls')),
    path('api/careers/', include('careers.urls')),
    path('api/gallery/', include('gallery.urls')),
    path("api/network/", include('our_network.urls')),
    #documentation_swagger
    path('documentation/', include('documentation.urls'))
] 

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)