from django.contrib import admin
from .models import *
from .forms import AlbumForm


class AlbumAdmin(admin.ModelAdmin):
    readonly_fields = ('creationDateTime',)
    list_display = ('name', "creationDateTime",
                    "releaseDateTime", "cost", "isApproved", "artist")
    fields = ['name', "artist", "creationDateTime",
                "releaseDateTime", "cost", "isApproved"]


admin.site.register(Album, AlbumAdmin, form=AlbumForm)