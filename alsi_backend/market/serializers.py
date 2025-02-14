from rest_framework import serializers
from .models import BlogBanner, BlogEntry

class BlogBannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogBanner
        fields = '__all__'

class BlogEntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogEntry
        fields = ['id', 'image', 'blog_title', 'description', 'blog_slug', 'main_title', 'date', 'time', 'intro', 'additional_content']