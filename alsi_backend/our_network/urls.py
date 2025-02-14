from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import NetworkBannerViewSet, NetworkViewSet

router = DefaultRouter()
router.register(r'our-network-banner', NetworkBannerViewSet)
router.register(r'our-network', NetworkViewSet)

urlpatterns = [
    path('',include(router.urls))
]