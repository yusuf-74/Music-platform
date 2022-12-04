from rest_framework import serializers
from .models import *
from rest_framework.validators import UniqueValidator
from django.core.exceptions import ValidationError

def checkBlank(str):
    if str == '':
        raise ValidationError('null not allowed')

class ArtistSerializerForAlbum(serializers.ModelSerializer):
    stageName = serializers.CharField(
        max_length=100,
        validators=[checkBlank, UniqueValidator(queryset=Artist.objects.all())]
    )
    socialLink = serializers.URLField(max_length=250, validators=[checkBlank])

    class Meta:
        model = Artist
        exclude= ['user']



class SongSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(required=False)
    audioFile = serializers.FileField(required=False)
    

    class Meta:
        model = Song
        fields = '__all__'


class AlbumSerializer (serializers.ModelSerializer):
    isApproved = serializers.BooleanField(
        required=False, help_text="Approve the album if its name is not explicit")
    artist = ArtistSerializerForAlbum()
    songs = SongSerializer(many=True, required=False)
    class Meta:
        model = Album
        exclude = ['id']
        

class CreateAlbumSerializer (serializers.ModelSerializer):
    songs = SongSerializer(many=True, required=False)

    class Meta:
        model = Album
        exclude = ('isApproved',)
        
        
        
