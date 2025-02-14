from rest_framework import serializers
from .models import Banners, OurStory, OurTeam, OurTeamEntry, Mission, MissionEntry, Member, MemberEntry

class BannersSerializer(serializers.ModelSerializer):
    class Meta:
         model = Banners
         fields = '__all__'

class OurStorySerializer(serializers.ModelSerializer):

    class Meta:
        model = OurStory
        fields = ['id', 'title', 'image', 'description_first', 'description_second','description_third']

class OurTeamEntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = OurTeamEntry
        fields = ['id', 'name', 'position']  

class OurTeamSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = OurTeam
        fields = ['id', 'title'] 

class MissionEntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = MissionEntry
        fields = ['id', 'image', 'title', 'description'] 

class MissionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Mission
        fields = ['id', 'title']


class MemberEntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = MemberEntry
        fields = ['id', 'image']  

class MemberSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Member
        fields = ['id', 'title']
