from rest_framework import serializers
from .models import Footer

# Footer
class FooterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Footer
        fields = ['id', 'location', 'company', 'address', 'contact', 'email']