from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import FooterViewSet

router = DefaultRouter()
router.register(r'footer', FooterViewSet)

urlpatterns = [
    path('',include(router.urls))
]