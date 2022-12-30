from django import forms
from .models import *

class UserForm (forms.ModelForm):
    bio = forms.CharField(widget=forms.Textarea)
    class Meta:
        model = User
        fields = '__all__'
