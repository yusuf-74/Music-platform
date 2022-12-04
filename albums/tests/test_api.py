import pytest
from rest_framework.test import APIClient
from rest_framework import status
from ..models import Album, Song
from artists.models import Artist
from artists.serializers import ArtistSerializer
from datetime import datetime
pytestmark = pytest.mark.django_db

class TestAlbumAPI:
    def test_get(self):
        client = APIClient()
        response = client.get('/albums/')
        assert response.status_code == 200

    def test_post_with_not_artist_user(self):
        client = APIClient()
        artist = ArtistSerializer(
            data={"stageName": "TestName", "socialLink": "https://www.facebook.com/"})
        if artist.is_valid():
            artist.save()
        
        response = client.post('/albums/create/',
                                {
                                    "name": "my album"
                                },
                            format='json'
                            )
        albums = Album.objects.all()
        print(albums)
        assert response.status_code == 401
