from dataclasses import fields
from rest_framework import serializers

from .models import ExecInfo, HiddenInfoContainer, ImageInfo, TextInfo


class TextInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TextInfo
        fields = '__all__'

class ImageInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageInfo
        fields = '__all__'

class ExecInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExecInfo
        fields = '__all__'


class HiddenInfoContainerSerializer(serializers.ModelSerializer):
    class Meta:
        model = HiddenInfoContainer
        fields = '__all__'
