1. Remove any apps/views that we created from before that have to do with authenticating users
-  **Done**


2. Create an app users
```bash
django-admin startapp users
```

3.  In the users app, extend Django's user model by inheriting from AbstractUser to include an optional bio
CharField with a max length of 256 characters

***at users.models.py***
```python
from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    bio = models.CharField(max_length=256 , blank=True)
```

-  On django admin, this field should be displayed as a TextArea
***forms.py***
```py
from django import forms
from .models import *

class UserForm (forms.ModelForm):
    bio = forms.CharField(widget=forms.Textarea)
    class Meta:
        model = User
        fields = '__all__'
```
***admin.py***

```py
from django.contrib import admin
from .models import *
from .forms import *

class UserAdmin(admin.ModelAdmin):
    form = UserForm
    
admin.site.register(User , UserAdmin)
```

3. Create an app authentication

```bash
django-admin startapp users
```

4. In the authentication app, support a POST authentication/register/ endpoint that creates users.

***authentication.urls.py***
```py
from knox import views as knox_views
from .views import *
from django.urls import path
urlpatterns = [
     path('login/', LoginAPI.as_view(), name='knox_login'),
     path('register/', RegisterAPI.as_view(), name='knox_signup'),
     path('logout/', knox_views.LogoutView.as_view(), name='knox_logout'),
     path('logoutall/', knox_views.LogoutAllView.as_view(), name='knox_logoutall'),
]

```

-  Think about the suitable permission class(es) for this endpoint

**it should be allow any**

-  This endpoint must accept the following fields formatted in JSON:

***authentication.serializers.py***
```py
class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(validators=[])
    password1 = serializers.CharField(required=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'bio', 'email', 'password', 'password1']
        extra_kwargs = {'password': {'write_only': True}}

    def validate(self, data):
        user = User(username=data['username'],
                    email=data['email'],
                    password=data['password'])
        password = data.get('password')
        
        errors = dict()
        try:
            validators.validate_password(password=password, user=user)
        except exceptions.ValidationError as e:
            errors['password'] = list(e.messages)
            
        if errors:
            raise serializers.ValidationError(errors)
        else :
            return data

    def create(self, validated_data):
        if validated_data['password'] == validated_data['password1']:
            user = User.objects.create_user(
                username=validated_data['username'],
                email=validated_data['email'],
                password=validated_data['password']
            )
            return user
        raise serializers.ValidationError("passwords doesn't match")
```

***authentication.views.py***
```py
from rest_framework import generics, permissions
from rest_framework.response import Response
from knox.models import AuthToken
from .serializers import *
from users.serializers import *
from knox.auth import TokenAuthentication


class RegisterAPI(generics.GenericAPIView):
    serializer_class = RegisterSerializer
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            "user": UserSerializer(user, context=self.get_serializer_context()).data,
            "token": AuthToken.objects.create(user)[1]
        })
```
-  Perform proper validation on all fields including letting the user know if their password isn't strong enough or if
password1 doesn't match password2

```py
from users.models import User
from rest_framework import serializers
from django.contrib.auth import authenticate
from django.contrib.auth import password_validation as validators
from django.core import exceptions


def validate(self, data):
    user = User(username=data['username'],
                email=data['email'],
                password=data['password'])
    password = data.get('password')
    errors = dict()
    try:
        validators.validate_password(password=password, user=user)
    except exceptions.ValidationError as e:
        errors['password'] = list(e.messages)
        
    if errors:
        raise serializers.ValidationError(errors)
    else :
        return data
def create(self, validated_data):
    if validated_data['password'] == validated_data['password1']:
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        return user
    raise serializers.ValidationError("passwords doesn't match")
```
-  Make sure passwords are being hashed and email domains are stored in lowercase. (hint: use create_user )
**Done**

5. Create a POST authentication/login/ that logs in users using their username and password and returns a
KnoxToken and the user's data in a nested object.


***authentication.serializers.py***
```py
from users.models import User
from rest_framework import serializers
from django.contrib.auth import authenticate

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Incorrect Credentials")
```


***authentication.views.py***
```py
from rest_framework import generics, permissions
from rest_framework.response import Response
from knox.models import AuthToken
from .serializers import *
from users.serializers import *
from knox.auth import TokenAuthentication

class LoginAPI(generics.GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        token = AuthToken.objects.create(user)[1]
        return Response({
            "user": UserSerializer(user, context=self.get_serializer_context()).data,
            "token": token
        })
```
6. Create a POST authentication/logout/ endpoint that logs the user out from the app by invalidating the knox toke

**using knox_views**
```py
from knox import views as knox_views
from .views import *
from django.urls import path
urlpatterns = [
     path('login/', LoginAPI.as_view(), name='knox_login'),
     path('register/', RegisterAPI.as_view(), name='knox_signup'),
     path('logout/', knox_views.LogoutView.as_view(), name='knox_logout'),
     path('logoutall/', knox_views.LogoutAllView.as_view(), name='knox_logoutall'),
]
```

7. In the users app, create a user detail endpoint /users/<pk> that supports the following requests:


```py
from django.urls import path, include
from .views import *
from knox import views as knox_views ,urls
urlpatterns = [    
    path('<int:pk>/', GetAPI.as_view()),
]

```

- GET returns the user data matching the given pk , namely, it should return the user's id , username , email ,
and bio .

```py
def get(self, request, pk , *args, **kwargs):
    try:
        user = User.objects.get(id=pk)
    except:
        raise Http404("not found")
    return Response(UserSerializer(user).data)
```

- Support updating the bio , username , and email fields via the following requests:

  -  PUT This is exactly the same as when creating a user except that an ID of an existing user is provided in
    the URL, and that the request will overwrite the user's data with that given ID
  - PATCH This is exactly the same as when updating a user except none of the fields are required, and that
    only fields given a value will be updated. (hint: see partial_update in serializers)
  - Allow update requests if the user making the request is the user in the <pk> of the url.

```py
def put(self, request, pk, format=None):
    try:
        user = User.objects.get(id=pk)
    except:
        raise Http404("not found")
    serializer = UserSerializer(user, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def patch(self , request,pk , *args, **kwargs):
    try:
        user = User.objects.get(id=pk)
    except:
        raise Http404("not found")
    serializer = UserSerializer(user, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
```
8. Add TokenAuthentication to the default authentication classes
```py

REST_KNOX = {
  'SECURE_HASH_ALGORITHM': 'cryptography.hazmat.primitives.hashes.SHA512',
  'AUTH_TOKEN_CHARACTER_LENGTH': 64,
  'TOKEN_TTL': timedelta(hours=10),
  'USER_SERIALIZER': 'knox.serializers.UserSerializer',
  'TOKEN_LIMIT_PER_USER': None,
  'AUTO_REFRESH': False,
  'EXPIRY_DATETIME_FORMAT': api_settings.DATETIME_FORMAT,
}
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'knox.auth.TokenAuthentication',
    ]
}
```
