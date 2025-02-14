from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CareersBannerViewSet, CareersFormViewSet

router = DefaultRouter()
router.register(r'careers-banner', CareersBannerViewSet)
router.register(r'careers-form', CareersFormViewSet, basename='careers-form')

urlpatterns = [
    path('',include(router.urls))
]
