from rest_framework import serializers
from .models import CareersBanner, CareersForm

class CareersBannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = CareersBanner
        fields = '__all__'
        
class CareersFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = CareersForm
        fields = ['id', 'name', 'email', 'phone', 'message', 'referer_url', 'submitted_url', 'file']