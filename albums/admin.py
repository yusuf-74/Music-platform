from django.contrib import admin
from .models import *
from .forms import AlbumForm


class AlbumAdmin(admin.ModelAdmin):
    readonly_fields = ('created','modified')
    list_display = ('name', "created", 'modified',
                    "releaseDateTime", "cost", "isApproved", "artist")
    fields = ['name', "artist", "created", 'modified',
                "releaseDateTime", "cost", "isApproved"]


admin.site.register(Album, AlbumAdmin, form=AlbumForm )

