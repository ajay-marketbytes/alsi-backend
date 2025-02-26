from rest_framework import serializers
from .models import ContactBanner, ContactForm
from django_recaptcha.fields import ReCaptchaField

class ContactBannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactBanner
        fields = '__all__'
        
class ContactFormSerializer(serializers.ModelSerializer):
    captcha = ReCaptchaField()
    class Meta:
        model = ContactForm
        fields = ['id', 'name', 'email', 'phone', 'message', 'referer_url', 'submitted_url', 'submitted_at']