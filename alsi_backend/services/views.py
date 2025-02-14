from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from .models import ServicesTitle, Services, SpecializedService, SpecializedServiceBanner, Subcategory, Card,  SpecializedCategory, SpecializedCard
from .serializers import ServicesTitleSerializer, ServicesSerializer, SpecializedServiceSerializer, SpecializedServiceBannerSerializer, SubcategorySerializer, CardSerializer, SpecializedCategorySerializer,SpecializedCardSerializer

class ServicesTitleViewSet(viewsets.ModelViewSet):
    queryset = ServicesTitle.objects.all()
    serializer_class = ServicesTitleSerializer
    permission_classes = [AllowAny]

class ServicesViewSet(viewsets.ModelViewSet):
    queryset = Services.objects.prefetch_related('subcategories__cards').all()
    serializer_class = ServicesSerializer
    permission_classes = [AllowAny]
    lookup_field = 'link_url'

class SubcategoryViewSet(viewsets.ModelViewSet):
    queryset = Subcategory.objects.prefetch_related('cards').all()
    serializer_class = SubcategorySerializer
    permission_classes = [AllowAny]

class CardViewSet(viewsets.ModelViewSet):
    queryset = Card.objects.all()
    serializer_class = CardSerializer
    permission_classes = [AllowAny]
    lookup_field = 'id'

class SpecializedServiceBannerViewSet(viewsets.ModelViewSet):
    queryset = SpecializedServiceBanner.objects.all()
    serializer_class = SpecializedServiceBannerSerializer
    permission_classes = [AllowAny]

class SpecializedServiceViewSet(viewsets.ModelViewSet):
    queryset = SpecializedService.objects.all()
    serializer_class = SpecializedServiceSerializer
    permission_classes = [AllowAny]
    lookup_field = 'link_url'

class SpecializedCategoryViewSet(viewsets.ModelViewSet):
    queryset = SpecializedCategory.objects.prefetch_related('cards').all()
    serializer_class = SpecializedCategorySerializer
    permission_classes = [AllowAny]

class SpecializedCardViewSet(viewsets.ModelViewSet):
    queryset = SpecializedCard.objects.all()
    serializer_class = SpecializedCardSerializer
    permission_classes = [AllowAny]
    lookup_field = 'id'