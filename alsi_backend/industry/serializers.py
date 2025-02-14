from rest_framework import serializers
from .models import IndustryBanner, IndustryEntry

class IndustryEntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = IndustryEntry
        fields = ['id', 'title', 'description', 'image'] 
        ref_name = "IndustryIndustryEntry"

class IndustryBannerSerializer(serializers.ModelSerializer):
    class Meta:
        model =IndustryBanner
        fields = ['id','title', 'image']