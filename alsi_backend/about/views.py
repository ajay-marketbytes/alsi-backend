from rest_framework import viewsets
from .serializers import BannersSerializer, OurStorySerializer, OurTeamSerializer, OurTeamEntrySerializer, MissionEntrySerializer, MissionSerializer, MemberEntrySerializer, MemberSerializer
from .models import Banners, OurStory, OurTeamEntry, OurTeam, MissionEntry, Mission, MemberEntry, Member
from rest_framework.permissions import AllowAny

class BannerViewSet(viewsets.ModelViewSet):
    queryset = Banners.objects.all()
    serializer_class = BannersSerializer
    permission_classes = [AllowAny]

class OurStoryViewSet(viewsets.ModelViewSet):
    queryset = OurStory.objects.all()
    serializer_class = OurStorySerializer
    permission_classes = [AllowAny]

class OurTeamEntryViewSet(viewsets.ModelViewSet):
    queryset = OurTeamEntry.objects.all() 
    serializer_class = OurTeamEntrySerializer
    permission_classes = [AllowAny]

class OurTeamViewSet(viewsets.ModelViewSet):
    queryset = OurTeam.objects.all() 
    serializer_class = OurTeamSerializer
    permission_classes = [AllowAny]

class MissionEntryViewSet(viewsets.ModelViewSet):
    queryset = MissionEntry.objects.all()  
    serializer_class = MissionEntrySerializer
    permission_classes = [AllowAny]

class MissionViewSet(viewsets.ModelViewSet):
    queryset = Mission.objects.all()
    serializer_class = MissionSerializer
    permission_classes = [AllowAny]


class MemberEntryViewSet(viewsets.ModelViewSet):
    queryset = MemberEntry.objects.all()
    serializer_class = MemberEntrySerializer
    permission_classes = [AllowAny] 

class MemberViewSet(viewsets.ModelViewSet):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer
    permission_classes = [AllowAny]
