from django.db import models

# Create your models here.

class memeData(models.Model):

    """"Database model for storing meme info"""

    name = models.CharField(max_length=100)
    caption  = models.CharField(max_length=255)
    url  = models.URLField(max_length=200)
    

    def __str__(self):
        """Returns string representation of model"""
        return self.name

