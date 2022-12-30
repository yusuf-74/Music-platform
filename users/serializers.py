from .models import User
from rest_framework import serializers
from django.contrib.auth import authenticate ,login


# user serializer
class UserSerializer(serializers.ModelSerializer):
    bio = serializers.CharField(required=False)
    class Meta:
        model = User
        fields = ['id', 'username','bio', 'email']
