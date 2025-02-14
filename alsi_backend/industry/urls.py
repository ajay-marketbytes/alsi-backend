from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import IndustryBannerViewSet,IndustryEntryViewSet

router = DefaultRouter()

router.register(r'industry-banner', IndustryBannerViewSet)
router.register(r'industry-entries',IndustryEntryViewSet)

urlpatterns = [
    path('',include(router.urls)) 
]