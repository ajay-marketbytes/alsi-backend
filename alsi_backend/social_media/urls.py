from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import SocialMediaViewSet

router = DefaultRouter()
router.register(r'social-media-entries', SocialMediaViewSet)

urlpatterns = [
    path('',include(router.urls))
]