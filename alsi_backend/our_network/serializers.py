from rest_framework import serializers
from .models import NetworkBanner, Network

class NetworkBannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = NetworkBanner
        fields = '__all__'

class NetworkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Network
        fields = [
            'id', 
            'name', 
            'address', 
            'url', 
            'position_top', 
            'position_left', 
            'location', 
            'company_name',
            'fax', 
            'contact_name', 
            'position', 
            'phone', 
            'email',
        ]