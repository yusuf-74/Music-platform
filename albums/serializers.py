from rest_framework import serializers
from .models import *

class AlbumSerializer (serializers.ModelSerializer):
    isApproved = serializers.BooleanField(
        required=False, help_text="Approve the album if its name is not explicit")
    class Meta:
        model = Album
        fields = '__all__'
        

class SongSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(required=True)
    audioFile = serializers.FileField(required=True)

    class Meta:
        model = Song
        fields = '__all__'
