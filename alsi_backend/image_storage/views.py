from rest_framework import viewsets
from .models import UploadedImage
from .serializers import UploadedImageSerializer
from rest_framework.permissions import AllowAny

class UploadedImageViewSet(viewsets.ModelViewSet):
    queryset = UploadedImage.objects.all()
    serializer_class = UploadedImageSerializer
    permission_classes = [AllowAny]
