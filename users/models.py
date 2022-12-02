from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    bio = models.CharField(max_length=256 , blank=True)

    def __str__(self): 
        return self.username
