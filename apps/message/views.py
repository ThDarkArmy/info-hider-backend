from copy import error
from django.conf import settings
from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import DecryptedMessage, EncryptedMessage, Message
from .serializers import MessageSerializer, EncryptedMessageSerializer, DecryptedMessageSerializer
from django.http import FileResponse, HttpResponse
from django.core.serializers import serialize
from django.core.files import File
import io
from PIL import Image
import sys
import os

from django.core.files.uploadedfile import InMemoryUploadedFile
import json


@api_view(['GET'])
def getAll(request):
    messages = Message.objects.all()
    print(messages)
    serializer = MessageSerializer(messages, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getById(request, pk):
    user = Message.objects.get(id=pk)
    serializer = MessageSerializer(user, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def encryptMessage(request):
    serializer = MessageSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        print(serializer.data['textMsg'].encode())
        imageFile = open(str(settings.BASE_DIR) +
                         str(serializer.data['image1']), 'ab')
        if serializer.data['image2'] != None:
            img = Image.open(str(settings.BASE_DIR) + str(serializer.data['image2']))
            byte_array = io.BytesIO()
            img.save(byte_array, format='PNG')

            imageFile.write(byte_array.getvalue())
        elif serializer.data['textMsg'] != None:
            imageFile.write(serializer.data['textMsg'].encode())
        else:
            return Response({"success": False, "message": "Invalid request body", "error": "error occured"})

        imageFile.close()

        # encryptedMessage = EncryptedMessage.objects.create()
        # print(serializer.data['image1'])

        # img = Image.open(str(settings.BASE_DIR) +
        #                  str(serializer.data['image1']), 'r')
        # img_ext = list(os.path.splitext(img.filename))[-1]
        # img_io = io.BytesIO()
        # img.save(img_io, format="JPEG")
        # encryptedMessage.encryptedImage = InMemoryUploadedFile(img_io,
        #                                               'ImageField',
        #                                               'encrypted'+img_ext,
        #                                               'JPEG',
        #                                               sys.getsizeof(img_io), None)

        # encryptedMessage.save()

        # img.close()

        # encryptedMessageSerializer = EncryptedMessageSerializer(
        #     EncryptedMessage.objects.get(id=encryptedMessage.id), many=False)

        # img_file = open(str(settings.BASE_DIR)+str(encryptedMessageSerializer.data['encryptedImage']), 'rb')
        # content = img_file.read()
        # offset = content.index(bytes.fromhex('FFD9'))
        # img_file.seek(offset + 2)
        # print(img_file.read())

        # img_file.close()
        return Response({"success": True,
            "message": "Information Encrypted Successfully",
            "body": serializer.data})

    return Response("Invalid")


@api_view(['POST'])
def decryptMessage(request):
    decryptedImagePath = str(settings.BASE_DIR)+str("/media/images/info/"+"decryptedImage.jpg")
    serializer = EncryptedMessageSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    print(serializer.data['encryptedImage'])

    encryptedImage = open(str(settings.BASE_DIR) +
                          str(serializer.data['encryptedImage']), 'rb')
    content = encryptedImage.read()
    offset = content.index(bytes.fromhex("FFD9"))
    encryptedImage.seek(offset+2)

    decryptedImage = Image.open(io.BytesIO(encryptedImage.read()))
    decryptedImage.save(decryptedImagePath)

    decryptedImageFile = Image.open(decryptedImagePath, 'r')
    decryptedMessage = DecryptedMessage()
    img_io = io.BytesIO()
    img_ext = list(os.path.splitext(decryptedImageFile.filename))[-1]
    decryptedImageFile.save(img_io, format="JPEG")
    print(decryptedImageFile.filename)
    decryptedMessage.decryptedImage = InMemoryUploadedFile(img_io,
                                                      'ImageField',
                                                      'decrypted'+ img_ext,
                                                      'JPEG',
                                                      sys.getsizeof(img_io), None)


    decryptedMessage.save()

    decryptedMessageObject = DecryptedMessage.objects.get(id=decryptedMessage.id)
    decryptedMessageSerializer = DecryptedMessageSerializer(decryptedMessageObject, many=False)


    return Response(decryptedMessageSerializer.data)
