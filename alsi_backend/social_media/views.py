from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from .models import SocialMedia
from .serializers import SocialMediaSerializer

class SocialMediaViewSet(viewsets.ModelViewSet):
    queryset = SocialMedia.objects.all()
    serializer_class = SocialMediaSerializer
    permission_classes = [AllowAny]