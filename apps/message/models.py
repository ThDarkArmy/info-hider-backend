from distutils.command.upload import upload
from sre_constants import MAX_UNTIL
from django.db import models


# Create your models here.

class Message(models.Model):
    textMsg = models.CharField(max_length=5000, blank=True)
    image1 = models.ImageField(upload_to="images/front", blank=True)
    image2 = models.ImageField(upload_to="images/info", blank=True)

    def __str__(self):
        return ' textMsg: {} image1: {} image2: {}'.format(self.textMsg, self.image1, self.image2)


class EncryptedMessage(models.Model):
    encryptedImage = models.ImageField(upload_to="images/encrypted", blank=True)

    def __str__(self):
        return 'image: {}'.format(self.image)


class DecryptedMessage(models.Model):
    decryptedText = models.CharField(max_length=10000, blank=True)
    decryptedImage = models.ImageField(upload_to="images/decrypted", blank=True)

