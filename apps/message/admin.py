import imp
from django.contrib import admin
from .models import Message, EncryptedMessage, DecryptedMessage

# Register your models here.
class MessageAdmin(admin.ModelAdmin):
    list_display = ['id', 'textMsg', 'image1','image2']

class EncryptedMessageAdmin(admin.ModelAdmin):
    list_display = ['id', 'encryptedImage']

class DecryptedMessageAdmin(admin.ModelAdmin):
    list_display = ['id', 'decryptedText', 'decryptedImage']


admin.site.register(Message, MessageAdmin)
admin.site.register(EncryptedMessage, EncryptedMessageAdmin)
admin.site.register(DecryptedMessage, DecryptedMessageAdmin)