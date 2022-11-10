from django import forms
from .models import Album


class AlbumForm(forms.ModelForm):
    isApproved = forms.BooleanField(
        required=False, help_text="Approve the album if its name is not explicit")
    class Meta:
        model = Album
        fields = ['name' , 'cost' , 'releaseDateTime']
