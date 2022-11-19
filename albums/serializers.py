from rest_framework import serializers
from .models import *


class SongSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(required=True)
    audioFile = serializers.FileField(required=True)
    

    class Meta:
        model = Song
        fields = '__all__'


class AlbumSerializer (serializers.ModelSerializer):
    isApproved = serializers.BooleanField(
        required=False, help_text="Approve the album if its name is not explicit")
    songs = SongSerializer(many=True, required=False)
    class Meta:
        model = Album
        fields = '__all__'
        
