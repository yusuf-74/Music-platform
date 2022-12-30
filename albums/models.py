from django.db import models
from artists.models import *
from datetime import datetime
from model_utils.models import TimeStampedModel
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill


class AlbumQuery (models.QuerySet):
    def is_approved(self):
        return self.filter(isApproved=True)

    def search(self, q):
        return self.filter(name__icontains=q)


class Album(TimeStampedModel):
    name = models.CharField(
        max_length=150,
        default='New Album'
    )

    artist = models.ForeignKey(
        Artist,
        on_delete=models.CASCADE,
        related_name='albums')

    creationDateTime = models.DateTimeField(
        default=datetime.now,
        verbose_name='created on')

    releaseDateTime = models.DateTimeField(
        default=datetime.now, blank=False,
        verbose_name='released on')

    cost = models.DecimalField(
        max_digits=7,
        decimal_places=2,
        blank=False)

    isApproved = models.BooleanField(default=False, verbose_name='Approved')
    objects = models.Manager()
    custom = AlbumQuery.as_manager()

    def __str__(self):
        return self.name


class Song(models.Model):
    name = models.CharField(
        max_length=150,
        default='New Song'
    )
    image = models.ImageField(upload_to='songs/%y/%m/%d')

    thumbnailImage = ImageSpecField(source='image',
                                    processors=[ResizeToFill(100, 50)],
                                    format='JPEG',
                                    options={'quality': 60})

    album = models.ForeignKey(Album,
                              on_delete=models.PROTECT,
                              related_name='songs')

    audioFile = models.FileField(upload_to='audio/%y/%m/%d')

    def __str__(self):
        return self.name
