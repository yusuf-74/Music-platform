from users.models import User
from rest_framework import serializers
from django.contrib.auth import authenticate
from django.contrib.auth import password_validation as validators
from django.core import exceptions


# register serializer
class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True)
    password = serializers.CharField(validators=[])
    password1 = serializers.CharField(required=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'bio', 'email', 'password', 'password1']
        extra_kwargs = {'password': {'write_only': True}}
    
    def validate(self, data):
        # here data has all the fields which have validated values
        # so we can create a User instance out of it
        user = User(username=data['username'],
                    email=data['email'],
                    password=data['password'])

        # get the password from the data
        password = data.get('password')

        errors = dict()
        try:
            # validate the password and catch the exception
            validators.validate_password(password=password, user=user)
        # the exception raised here is different than serializers.ValidationError
        except exceptions.ValidationError as e:
            errors['password'] = list(e.messages)
        if errors:
            raise serializers.ValidationError(errors)
        return super(RegisterSerializer, self).validate(data)
    
    def create(self, validated_data):
        if validated_data['password'] == validated_data['password1']:
            user = User.objects.create_user(
                username=validated_data['username'],
                email=validated_data['email'],
                password=validated_data['password']
            )
            return user
        raise serializers.ValidationError("passwords doesn't match")

# login serializer


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Incorrect Credentials")
