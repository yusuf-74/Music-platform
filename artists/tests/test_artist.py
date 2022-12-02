import pytest
from ..models import Artist
from artists.serializers import ArtistSerializer
pytestmark = pytest.mark.django_db


class TestArtists:
    def test_creation_with_wrong_data(self):
        artist = ArtistSerializer(data={})
        assert artist.is_valid() == False

    def test_creation_with_correct_data(self):
        artist = Artist()
        artist.stageName = "Anas"
        artist.socialLink = "www.facebook.com/anashagras"
        artist.save()
        assert len(Artist.objects.all()) == 1
