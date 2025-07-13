from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.

class Trainer(models.Model):
    name = models.CharField(max_length=255)
    instagram = models.URLField()
    facebook = models.URLField()
    twitter = models.URLField()
    image = CloudinaryField("image")

    def __str__(self):
        return self.name
