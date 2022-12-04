import django_filters
from artists.models import *
class ArtistFilter(django_filters.FilterSet):
    stageName = django_filters.CharFilter(lookup_expr='icontains')
    albums__name = django_filters.CharFilter(lookup_expr='icontains')
    class Meta:
        model = Artist        
        fields = ['stageName' , 'socialLink','albums__name']