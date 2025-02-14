from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from .models import Footer
from .serializers import FooterSerializer

# Footer
class FooterViewSet(viewsets.ModelViewSet):
    queryset = Footer.objects.all()
    serializer_class = FooterSerializer
    permission_classes = [AllowAny]