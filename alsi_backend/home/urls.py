from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BannerViewSet, ChooseViewSet, DifferentiatorViewSet, DifferentiatorEntryViewSet, AchievementViewSet, AchievementEntryViewSet, HighlightViewSet, HighlightEntryViewSet, IndustryViewSet, IndustryEntryViewSet

router = DefaultRouter()
router.register(r'banner', BannerViewSet)
router.register(r'chooses', ChooseViewSet)
router.register(r'differentiator', DifferentiatorViewSet)
router.register(r'differentiator-entries', DifferentiatorEntryViewSet)
router.register(r'achievement', AchievementViewSet)
router.register(r'achievement-entries', AchievementEntryViewSet)
router.register(r'highlight', HighlightViewSet)
router.register(r'highlight-entries', HighlightEntryViewSet)
router.register(r'industry', IndustryViewSet)
router.register(r'industry-entries', IndustryEntryViewSet)

urlpatterns = [
    path('',include(router.urls))
]