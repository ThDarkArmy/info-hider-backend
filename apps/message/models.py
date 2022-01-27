from distutils.command.upload import upload
from django.db import models

# Create your models here.

class Message(models.Model):
    textMsg = models.CharField(max_length=5000)
    image1 = models.ImageField(upload_to="images", blank=True)
    image2 = models.ImageField(upload_to="images", blank=True)
