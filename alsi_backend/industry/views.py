from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from .serializers import IndustryEntrySerializer,IndustryBannerSerializer
from .models import IndustryBanner,IndustryEntry

class IndustryEntryViewSet(viewsets.ModelViewSet):
    queryset = IndustryEntry.objects.all()
    serializer_class = IndustryEntrySerializer
    permission_classes = [AllowAny]

class IndustryBannerViewSet(viewsets.ModelViewSet):
    queryset = IndustryBanner.objects.all()
    serializer_class = IndustryBannerSerializer
    permission_classes = [AllowAny]