from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import BannerViewSet, OurStoryViewSet, OurTeamEntryViewSet, OurTeamViewSet, MissionEntryViewSet, MissionViewSet, MemberEntryViewSet, MemberViewSet

router=DefaultRouter()
router.register(r'banner', BannerViewSet)
router.register(r'our-story', OurStoryViewSet, basename='OurStory')
router.register(r'our-team', OurTeamViewSet)  
router.register(r'our-team-entries', OurTeamEntryViewSet)
router.register(r'mission', MissionViewSet)  
router.register(r'mission-entries', MissionEntryViewSet) 
router.register(r'member', MemberViewSet)
router.register(r'member-entries', MemberEntryViewSet) 

urlpatterns = [
    path('',include(router.urls))
]