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
        response = client.get('/albums/create/')
        assert response.status_code == 200

    def test_post_with_wrong_data(self):
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
        assert response.status_code == 400

    def test_post_with_correct_data(self):
        client = APIClient()
        artist = ArtistSerializer(
            data={"stageName": "TestName", "socialLink": "https://www.facebook.com/"})
        if artist.is_valid():
            artist.save()
        response = client.post('/albums/create/',
                                    {
                                        "name": "my album",
                                        "artist": artist.data['id'],
                                        'cost' : 200,
                                        'releaseDateTime': datetime.strptime("12/11/2023 09:15:32",  "%d/%m/%Y %H:%M:%S")
                                    },
                                    format='json'
                                    )
        assert response.status_code == 201
        
    