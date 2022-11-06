from django.db import models 

class Artist(models.Model):
    stageName = models.CharField(max_length=100, unique=True ,verbose_name = 'Name')
    socialLink = models.URLField(max_length=250, blank=True , verbose_name = 'social media')        
    
    @property
    def Approved_Albums(self):
        return str(len(self.albums.filter(isApproved=True)))
    
    def __str__ (self):
        return self.stageName
        
    class Meta:
        ordering = ['stageName']
