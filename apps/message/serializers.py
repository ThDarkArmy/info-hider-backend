from dataclasses import field
from rest_framework import serializers

from .models import Message, EncryptedMessage, DecryptedMessage

class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = '__all__'

class EncryptedMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = EncryptedMessage
        fields = '__all__'


class DecryptedMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = DecryptedMessage
        fields = '__all__'

