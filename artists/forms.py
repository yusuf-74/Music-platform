from django import forms
from django.core.exceptions import ValidationError
from .models import Artist
from albums.forms import *
from django.core.validators import RegexValidator

URL_VALIDATOR = RegexValidator(
    regex='/([\da-z\.-]+)\.([a-z\.]{2,6})([\/\w \.-]*)*\/?$/', message='validation error')


def checkBlank(str):
    if str == '':
        raise ValidationError('null not allowed')


class ArtistForm(forms.ModelForm):
    stageName = forms.CharField(
        max_length=100,
        validators=[checkBlank]
    )
    socialLink = forms.URLField(max_length=250, validators=[checkBlank])

    class Meta:
        model = Artist
        fields = '__all__'
