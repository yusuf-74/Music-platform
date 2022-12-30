from django.db import models 
from users.models import User

class Artist(models.Model):
    stageName = models.CharField(max_length=100, unique=True ,verbose_name = 'Name')
    socialLink = models.URLField(max_length=250, verbose_name = 'social media')      
    user = models.OneToOneField(User, on_delete=models.CASCADE ,related_name = 'artist')
    
    @property
    def Approved_Albums(self):
        return str(len(self.albums.filter(isApproved=True)))
    
    def __str__ (self):
        return self.stageName
        
    class Meta:
        ordering = ['stageName']
