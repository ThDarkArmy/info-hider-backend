import imp
from django.contrib import admin
from .models import Message

# Register your models here.
class MessageAdmin(admin.ModelAdmin):
    list_display = ['id', 'textMsg', 'image1','image2']

admin.site.register(Message, MessageAdmin)