from django.contrib import admin
from .models import *
from .forms import *


class AlbumAdmin(admin.ModelAdmin):
    readonly_fields = ('created','modified')
    list_display = ('name', "created", 'modified',
                    "releaseDateTime", "cost", "isApproved", "artist")
    fields = ['name', "artist", "created", 'modified',
                "releaseDateTime", "cost", "isApproved"]


class SongAdmin(admin.ModelAdmin):
    list_display = ('name', "album")
    fields = ['name', "album"]

admin.site.register(Album, AlbumAdmin, form=AlbumForm )
admin.site.register(Song, form=SongForm)

