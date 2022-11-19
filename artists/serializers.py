from rest_framework import serializers
from .models import *
from django.core.exceptions import ValidationError
from albums.serializers import AlbumSerializer
from rest_framework.validators import UniqueValidator

def checkBlank(str):
    if str == '':
        raise ValidationError('null not allowed')


class ArtistSerializer(serializers.ModelSerializer):
    stageName = serializers.CharField(
        max_length=100,
        validators=[checkBlank ,UniqueValidator(queryset=Artist.objects.all())]
    )
    socialLink = serializers.URLField(max_length=250, validators=[checkBlank])
    
    albums = AlbumSerializer(many = True , required = False)

    class Meta:
        model = Artist
        fields = '__all__'
