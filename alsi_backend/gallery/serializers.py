from rest_framework import serializers
from .models import GalleryBanner, Gallery, GalleryImage, GalleryVideo

class GalleryBannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = GalleryBanner
        fields = '__all__'

class GalleryImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = GalleryImage
        fields = ['id', 'image','gallery']

class GalleryVideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = GalleryVideo
        fields = ['id', 'video_url', 'thumbnail','gallery']

class GallerySerializer(serializers.ModelSerializer):
    images = GalleryImageSerializer(many=True, read_only=True)
    videos = GalleryVideoSerializer(many=True, read_only=True)

    class Meta:
        model = Gallery
        fields = ['id', 'title', 'main_title', 'image', 'year', 'slug', 'images', 'videos']
