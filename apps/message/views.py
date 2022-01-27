from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Message
from .serializers import MessageSerializer
from apps.message import serializers

@api_view(['GET'])
def getAll(request):
    messages = Message.objects.all()
    serializer = MessageSerializer(messages, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getById(request, pk):
    user = Message.objects.get(id=pk)
    serializer = MessageSerializer(user, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def createEncryptedMessage(request):
    serializer = MessageSerializer(data=request.data)
    print("create encrypted message")

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['PUT'])
def updateUser(request, pk):
    user = Message.objects.get(id=pk)
    serializer = MessageSerializer(instance=user, data=request.data)   

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['DELETE'])
def deleteUser(request, pk):
    user = Message.objects.get(id=pk)
    user.delete()

    return Response("Message deleted successfully")

    


