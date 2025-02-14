from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ContactBannerViewSet, ContactFormViewSet

router = DefaultRouter()
router.register(r'contact-banner', ContactBannerViewSet)
router.register(r'contact-form', ContactFormViewSet, basename='contact-form')

urlpatterns = [
    path('',include(router.urls))
]
