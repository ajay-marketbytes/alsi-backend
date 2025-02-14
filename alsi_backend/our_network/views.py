from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from .models import NetworkBanner, Network
from .serializers import NetworkBannerSerializer, NetworkSerializer

class NetworkBannerViewSet(viewsets.ModelViewSet):
    queryset = NetworkBanner.objects.all()
    serializer_class = NetworkBannerSerializer
    permission_classes = [AllowAny]

class NetworkViewSet(viewsets.ModelViewSet):
    queryset = Network.objects.all()
    serializer_class = NetworkSerializer
    permission_classes = [AllowAny]
