from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from .models import GalleryBanner, Gallery, GalleryImage, GalleryVideo
from .serializers import GalleryBannerSerializer, GallerySerializer, GalleryImageSerializer, GalleryVideoSerializer

class GalleryBannerViewSet(viewsets.ModelViewSet):
    queryset = GalleryBanner.objects.all()
    serializer_class = GalleryBannerSerializer
    permission_classes = [AllowAny]

class GalleryViewSet(viewsets.ModelViewSet):
    queryset = Gallery.objects.all()
    serializer_class = GallerySerializer
    permission_classes = [AllowAny]
    lookup_field = 'slug'

class GalleryImageViewSet(viewsets.ModelViewSet):
    queryset = GalleryImage.objects.all()
    serializer_class = GalleryImageSerializer
    permission_classes = [AllowAny]

class GalleryVideoViewSet(viewsets.ModelViewSet):
    queryset = GalleryVideo.objects.all()
    serializer_class = GalleryVideoSerializer
    permission_classes = [AllowAny]
