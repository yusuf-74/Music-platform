import pytest
from albums.models import *
from artists.models import Artist
pytestmark = pytest.mark.django_db

class TestAlbum:
    def test_create_album_with_invalid_data(self):
        artist = Artist()
        artist.stageName = 'Hommos'
        artist.socialLink = 'https://www.hommos.com'
        artist.save()
        album = Album()
        album.name = "FirstAlbum"
        album.artist = artist
        
        with pytest.raises(Exception):
            album.save()
        
    def test_create_album_with_proper_data(self):
        artist = Artist()
        artist.stageName = 'Hommos'
        artist.socialLink = 'https://www.hommos.com'
        artist.save()
        album = Album(name='hola', cost=123, releaseDateTime=datetime.strptime(
            "12/11/2023 09:15:32",  "%d/%m/%Y %H:%M:%S"))
        album.artist = artist
        album.save()
        assert len(Album.objects.all()) == 1
        

class TestSong:
    def create_song_with_invalid_data(self):
        artist = Artist(stageName='Hommos',
                        socialLink='https://www.hommos.com').save()
        album = Album(name='hola', artist=artist, cost=123).save()
        song = Song()
        song.album = artist
        song.name = 'hola'

        with pytest.raises(Exception):
            song.save()