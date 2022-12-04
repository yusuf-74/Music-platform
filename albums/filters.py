import django_filters
from albums.models import *


class AlbumFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains')
    min_cost = django_filters.NumberFilter(field_name="cost",lookup_expr='gte')
    max_cost = django_filters.NumberFilter(field_name="cost",lookup_expr='lt')

    class Meta:
        model = Album
        fields = ['name', 'min_cost', 'max_cost']
