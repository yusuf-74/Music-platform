from django.db import models
from artists.models import *
from datetime import datetime
from model_utils.models import TimeStampedModel




class Album(TimeStampedModel):
    name = models.CharField(
        max_length=150,
        default='New Album'
        )
    
    artist = models.ForeignKey(
        Artist,
        on_delete=models.CASCADE,
        related_name = 'albums')
    
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
    
    isApproved = models.BooleanField(default = False , verbose_name = 'Approved')
    
    def __str__(self):
        return self.name
