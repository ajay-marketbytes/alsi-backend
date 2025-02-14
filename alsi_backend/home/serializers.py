from rest_framework import serializers
from .models import Banner, ChooseUs, Differentiator, DifferentiatorEntry, Achievement, AchievementEntry, Highlight, HighlightEntry, Industry, IndustryEntry

# Banner
class BannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Banner
        fields = '__all__'

# Choose Us
class ChooseSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChooseUs
        fields = '__all__'

# Differentiators
class DifferentiatorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Differentiator
        fields = '__all__'

class DifferentiatorEntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = DifferentiatorEntry
        fields = ['id', 'image', 'differentiator_title']

# Achievements
class AchievementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Achievement
        fields = '__all__'

class AchievementEntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = AchievementEntry
        fields = ['id', 'image', 'description']

# Highlights
class HighlightSerializer(serializers.ModelSerializer):
    class Meta:
        model = Highlight
        fields = '__all__'

class HighlightEntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = HighlightEntry
        fields = ['id', 'highlight_title']

# Industries
class IndustrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Industry
        fields = '__all__'
        ref_name = "HomeIndustryEntry"

class IndustryEntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = IndustryEntry
        fields = ['id', 'entry_number', 'image', 'title', 'description', 'path_name']
