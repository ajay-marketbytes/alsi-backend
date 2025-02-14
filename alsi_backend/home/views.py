from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from .models import Banner, ChooseUs, Differentiator, DifferentiatorEntry, Achievement, AchievementEntry, Highlight, HighlightEntry
from .serializers import BannerSerializer, ChooseSerializer, DifferentiatorSerializer, DifferentiatorEntrySerializer, AchievementSerializer, AchievementEntrySerializer, HighlightSerializer, HighlightEntrySerializer, Industry, IndustrySerializer, IndustryEntry, IndustryEntrySerializer

# Banner
class BannerViewSet(viewsets.ModelViewSet):
    queryset = Banner.objects.all()
    serializer_class = BannerSerializer
    permission_classes = [AllowAny]

# Choose Us
class ChooseViewSet(viewsets.ModelViewSet):
    queryset = ChooseUs.objects.all()
    serializer_class = ChooseSerializer
    permission_classes = [AllowAny]

# Differentiators
class DifferentiatorViewSet(viewsets.ModelViewSet):
    queryset = Differentiator.objects.all()
    serializer_class = DifferentiatorSerializer
    permission_classes = [AllowAny]

class DifferentiatorEntryViewSet(viewsets.ModelViewSet):
    queryset = DifferentiatorEntry.objects.all()
    serializer_class = DifferentiatorEntrySerializer
    permission_classes = [AllowAny]

# Achievements
class AchievementViewSet(viewsets.ModelViewSet):
    queryset = Achievement.objects.all()
    serializer_class = AchievementSerializer
    permission_classes = [AllowAny]

class AchievementEntryViewSet(viewsets.ModelViewSet):
    queryset = AchievementEntry.objects.all()
    serializer_class = AchievementEntrySerializer
    permission_classes = [AllowAny]

# Highlights
class HighlightViewSet(viewsets.ModelViewSet):
    queryset = Highlight.objects.all()
    serializer_class = HighlightSerializer
    permission_classes = [AllowAny]

class HighlightEntryViewSet(viewsets.ModelViewSet):
    queryset = HighlightEntry.objects.all()
    serializer_class = HighlightEntrySerializer
    permission_classes = [AllowAny]

# Industries
class IndustryViewSet(viewsets.ModelViewSet):
    queryset = Industry.objects.all()
    serializer_class = IndustrySerializer
    permission_classes = [AllowAny]

class IndustryEntryViewSet(viewsets.ModelViewSet):
    queryset = IndustryEntry.objects.all()
    serializer_class = IndustryEntrySerializer
    permission_classes = [AllowAny]
