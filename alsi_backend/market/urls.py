from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BlogBannerViewSet, BlogEntryViewSet

router = DefaultRouter()
router.register(r'blog-banner', BlogBannerViewSet)
router.register(r'blog-entries', BlogEntryViewSet)

urlpatterns = [
    path('',include(router.urls))
]