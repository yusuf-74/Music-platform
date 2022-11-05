from django.db import models


class Artist(models.Model):
    stageName = models.CharField(max_length=100, unique=True)
    socialLink = models.URLField(max_length=250, blank=True)

    def __str__ (self):
        return self.stageName
        
    class Meta:
        ordering = ['stageName']
