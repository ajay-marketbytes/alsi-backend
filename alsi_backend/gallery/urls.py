from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import GalleryBannerViewSet, GalleryViewSet, GalleryImageViewSet, GalleryVideoViewSet

router = DefaultRouter()
router.register(r'gallery-banner', GalleryBannerViewSet)
router.register(r'gallery-entries', GalleryViewSet)
router.register(r'gallery-images', GalleryImageViewSet)
router.register(r'gallery-videos', GalleryVideoViewSet)

urlpatterns = [
    path('',include(router.urls)),
]