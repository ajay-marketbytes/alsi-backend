from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ServicesTitleViewSet, ServicesViewSet, SpecializedServiceViewSet, SpecializedServiceBannerViewSet, SubcategoryViewSet, CardViewSet, SpecializedCategoryViewSet, SpecializedCardViewSet

router = DefaultRouter()
router.register(r'services-banner', ServicesTitleViewSet)
router.register(r'services', ServicesViewSet, basename='services')
router.register(r'subcategories', SubcategoryViewSet, basename='subcategories')
router.register(r'cards', CardViewSet, basename='cards')

router.register(r'specialized-banner', SpecializedServiceBannerViewSet)
router.register(r'specialized-entries', SpecializedServiceViewSet)
router.register(r'specialized-categories', SpecializedCategoryViewSet, basename="specializedcategory")
router.register(r'specialized-cards', SpecializedCardViewSet, basename="specializedcard")

urlpatterns = [
    path('', include(router.urls))
]
