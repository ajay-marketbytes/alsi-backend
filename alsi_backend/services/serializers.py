from rest_framework import serializers
from .models import ServicesTitle, Services, Card, Subcategory, SpecializedService, SpecializedServiceBanner,  SpecializedCategory, SpecializedCard
from rest_framework.exceptions import ValidationError

class ServicesTitleSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServicesTitle
        fields = '__all__'

class CardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Card
        fields = ['id', 'title', 'image', 'subcategory']


    def validate_subcategory(self, value):
        if not value:
            raise ValidationError("Subcategory is required.")
        return value


class SubcategorySerializer(serializers.ModelSerializer):
    cards = CardSerializer(many=True, read_only=True)
    service_id = serializers.PrimaryKeyRelatedField(queryset=Services.objects.all(), source='service', write_only=True)

    class Meta:
        model = Subcategory
        fields = ['id', 'title', 'text_color', 'enable_fill_empty_cards', 'cards', 'service_id']


class ServicesSerializer(serializers.ModelSerializer):
    subcategories = SubcategorySerializer(many=True, read_only=True)

    class Meta:
        model = Services
        fields = [
            'id', 'image', 'title', 'service_title', 'subtitle',
            'link_url', 'banner_image', 'content_paragraphs', 'subcategories'
        ]

class SpecializedServiceBannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = SpecializedServiceBanner
        fields = ['id','title', 'image']
    
class SpecializedCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = SpecializedCard
        fields = ['id', 'title', 'image', 'category']  

    def validate_category(self, value):
        if not value:
            raise ValidationError("Category is required.")
        return value

class SpecializedCategorySerializer(serializers.ModelSerializer):
    cards = SpecializedCardSerializer(many=True, read_only=True)
    service_id = serializers.PrimaryKeyRelatedField(queryset=SpecializedService.objects.all(), source='service', write_only=True)

    class Meta:
        model = SpecializedCategory
        fields = ['id', 'title', 'text_color', 'enable_fill_empty_cards', 'cards', 'service_id']

class SpecializedServiceSerializer(serializers.ModelSerializer):
    subcategories = SpecializedCategorySerializer(many=True, read_only=True)

    class Meta:
        model = SpecializedService
        fields = ['id', 'title', 'description', 'image', 'dedicated_title', 'dedicated_image', 'dedicated_paragraph', 'link_url', 'subcategories']