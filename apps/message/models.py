from django.db import models


# Create your models here.

class TextInfo(models.Model):
    textInfo = models.TextField(max_length=5000, blank=False)
    containerImage = models.ImageField(upload_to="images/containers", blank=False)


class ImageInfo(models.Model):
    imageInfo = models.ImageField(upload_to="images/info", blank=False)
    containerImage = models.ImageField(upload_to="images/containers", blank=False)


class ExecInfo(models.Model):
    execFile = models.FileField(upload_to="files/exec", blank=False)
    containerImage = models.ImageField(upload_to="images/containers", blank=False)


class HiddenInfoContainer(models.Model):
    hiddenInfoContainerImage = models.ImageField(upload_to="images/HiddenInfoContainers")


# class ExtractedInfo(models.Model):
#     extractedText = models.TextField(max_length=5000, blank=True)
#     extractedImage = models.ImageField(upload_to="images/extractedImages", blank=True)
#     extractedExecFile = models.FileField(upload_to="file/extractedExecFiles", blank=True)

