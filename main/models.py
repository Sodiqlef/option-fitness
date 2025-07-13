from django.db import models
from cloudinary import CloudinaryImage

# Create your models here.

class Trainer():
    name = models.CharField(max_length=255)
    instagram = models.URLField()
    facebook = models.URLField()
    twitter = models.URLField()
