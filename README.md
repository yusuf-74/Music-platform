1. Feel free to remove any non-API views that we created from before



2. Create a class-based view at the path /artists/ that returns a list of artists in JSON format for GET requests, the artist
data should include the following fields.

-  ***code***

```python
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class ArtistViewList (APIView):
    def get(self, request, format=None):
        artists = Artist.objects.all()
        serializer = ArtistSerializer(artists, many=True)
        return Response(serializer.data)
```

-  ***image***

<img src = './readme elements/get_artists.png' style = 'width : 800px; margin : 24px 0 48px 24px'/>



3.  The same view above should accept POST requests and accept all the fields on the artist model (excluding the id)

- Include proper validation for each field as listed on the artist model:
  - this field is required
  - this field value already exists (for unique fields)
- If the request passes the validation process, the given data should be used to create and save an artist instance

***code*** - **views.py**

```python
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class ArtistViewCreate(APIView):
    def get(self, request, format=None):
        artists = Artist.objects.all()
        serializer = ArtistSerializer(artists, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        serializer = ArtistSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

```
***code*** - **serializers.py**

```python
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

```
***image of*** **Bad request**

<img src = './readme elements/bad_post.png' style = 'width : 800px; margin : 24px 0 48px 24px'/>

***image of*** **good request**

<img src = './readme elements/good_post.png' style = 'width : 800px; margin : 24px 0 48px 24px'/>

5. You may want to use a tool to make the HTTP requests and inspect them, I personally use **Postman** but there are other
options like **curl** and **Insomnia**

**Done** : ***i used Postman***

