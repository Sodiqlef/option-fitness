from django.db import models
from django.contrib.auth.models import User
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

    

class Blog(models.Model):
    subject = models.CharField(max_length=255)
    message = models.TextField(max_length=4000)
    image = CloudinaryField("image")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True)

    def __str__(self):
        return self.name
    