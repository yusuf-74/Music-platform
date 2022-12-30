from django import forms
from .models import *


class AlbumForm(forms.ModelForm):
    isApproved = forms.BooleanField(
        required=False, help_text="Approve the album if its name is not explicit")
    class Meta:
        model = Album
        fields = ['name' , 'cost' , 'releaseDateTime']

class SongForm(forms.ModelForm):
    image = forms.ImageField(required=True)
    audioFile = forms.FileField(required=True)
    class Meta:
        model = Song
        fields = '__all__'
        