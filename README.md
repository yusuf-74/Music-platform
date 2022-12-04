1. Add a relationship field to the Artist model that maps an artist to a user instance.

```py
from django.db import models 
from users.models import User

class Artist(models.Model):
    stageName = models.CharField(max_length=100, unique=True ,verbose_name = 'Name')
    socialLink = models.URLField(max_length=250, verbose_name = 'social media')      
--> user = models.OneToOneField(User, on_delete=models.CASCADE ,related_name = 'artist') <--- 
```

2. GET should return a list of approved albums

  - responnse
```json
[
    {
        "id": 1,
        "isApproved": true,
        "artist": {
            "id": 1,
            "stageName": "yusuf",
            "socialLink": "https://www.srfes.com"
        },
        "songs": [],
        "created": "2022-12-04T14:23:20.295340Z",
        "modified": "2022-12-04T14:23:20.295340Z",
        "name": "approved",
        "creationDateTime": "2022-12-04T16:23:20.295340Z",
        "releaseDateTime": "2022-12-04T16:23:02Z",
        "cost": "250.00"
    }
]
```
  - Permit any type of request whether it's authenticated or not

  ```py
  from rest_framework.permissions import AllowAny


class ListAlbum(APIView):
    permission_classes = [AllowAny]
    
    ...etc
```

  - It doesn't make sense to return all albums that we have to the frontend at once, if we have hundreds of
thousands of albums, the user's screen will not be able to render that much data, instead we should
support pagination.
 

***settings.py***

```py
REST_FRAMEWORK = {
    ...

'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
    'PAGE_SIZE': 2,

    ...
    }
```

  - Bonus: Can you create and use custom queryset manager that only returns approved albums?


***albums.models.py***
```py
class AlbumQuery (models.QuerySet):
    def is_approved(self):
        return self.filter(isApproved=True)

    def search(self, q):
        return self.filter(name__icontains=q)
```
3. POST should accept a JSON body, create an album, and raise proper validation errors for all fields

 - The request body should look like: { "name": ..., "release_datetime": ..., "cost": ..., }
 - Permit only authenticated requests
 - The request must be authenticated by a user who is also an artist
 - The created album will be mapped to the artist who made the request
 - 403 Forbidden error should be raised if a POST request is not authenticated or if it's authenticated by a
user who isn't an artist

```py
class CreateAlbum(generics.CreateAPIView):
    def post(self, request):
        data = request.data
        user = request.user
        try:
            data ['artist'] = Artist.objects.get(user=user).pk
        except:
            return Response("user is not registered as artist" , status=status.HTTP_403_FORBIDDEN)
        
        serializer = CreateAlbumSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
```
4. Using django-filter , support the following optional filters for GET requests:
 - Cost greater than or equal
 - Cost less than or equal
 - Case-insensitive containment


***albums.filters.py***
```py
import django_filters
from albums.models import *


class AlbumFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains')
    min_cost = django_filters.NumberFilter(field_name="cost",lookup_expr='gte')
    max_cost = django_filters.NumberFilter(field_name="cost",lookup_expr='lt')

    class Meta:
        model = Album
        fields = ['name', 'min_cost', 'max_cost']

```

***albums.views.py***
 ```py
class ListAlbum(generics.ListAPIView):
    permission_classes = [AllowAny]
    authentication_classes = []
    queryset = Album.objects.all()
    filterset_class = AlbumFilter
    serializer_class = AlbumSerializer
 ```