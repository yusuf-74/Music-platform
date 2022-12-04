from django.contrib import admin
from .models import *


class ArtistAdmin(admin.ModelAdmin):
    readonly_fields = ('Approved_Albums',)
    list_display = ('stageName', 'socialLink', 'Approved_Albums')
    fields = ['stageName', 'socialLink', 'Approved_Albums','user']


admin.site.register(Artist, ArtistAdmin)
