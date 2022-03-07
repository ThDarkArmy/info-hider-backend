from django.conf import settings

from rest_framework.response import Response
from rest_framework.decorators import api_view

from .serializers import ExecInfoSerializer, HiddenInfoContainerSerializer, ImageInfoSerializer, TextInfoSerializer
import io
from PIL import Image
import uuid
import mimetypes



# @api_view(['GET'])
# def getAll(request):
#     messages = Message.objects.all()
#     print(messages)
#     serializer = MessageSerializer(messages, many=True)
#     return Response(serializer.data)


# @api_view(['GET'])
# def getById(request, pk):
#     user = Message.objects.get(id=pk)
#     serializer = MessageSerializer(user, many=False)
#     return Response(serializer.data)



# hide text in image
@api_view(['POST'])
def hideText(request):
    serializer = TextInfoSerializer(data=request.data)

    print(request.data)

    if serializer.is_valid():
        serializer.save()
        containerImageFile = open(str(settings.BASE_DIR)+ str(serializer.data['containerImage']), 'ab')
        containerImageFile.write(serializer.data['textInfo'].encode())

        return Response({"success": True,
            "message": "Information hided successfully",
            "body":{"containerImage": serializer.data["containerImage"]}})

    else:
        return Response({"success": False,
            "message": "Invalid request data"})


# hide image in another image
@api_view(['POST'])
def hideImage(request):
    serializer = ImageInfoSerializer(data=request.data)
    print(request.data)
    if serializer.is_valid():
        serializer.save()
        containerImageFile = open(str(settings.BASE_DIR)+ str(serializer.data['containerImage']), 'ab')
        imageInfoFile = Image.open(str(settings.BASE_DIR) + str(serializer.data['imageInfo']))
        byte_array = io.BytesIO()
        imageInfoFile.save(byte_array, format='PNG')

        containerImageFile.write(byte_array.getvalue())

        return Response({"success": True, "message": "Information hided successfully", "body":{"containerImage": serializer.data['containerImage']}})

    else:
        return Response({"success": False,
            "message": "Invalid request data"})


# hide execfile in an image
@api_view(['POST'])
def hideExec(request):
    serializer = ExecInfoSerializer(data=request.data)
    print(request.data)
    if serializer.is_valid():
        serializer.save()
        containerImageFile = open(str(settings.BASE_DIR)+ str(serializer.data['containerImage']), 'ab')
        execFile = open(str(settings.BASE_DIR)+str(serializer.data['execFile']), 'rb')

        containerImageFile.write(execFile.read())

        return Response({"success": True, "message": "Info hided successfully", "body":{"containerImage": serializer.data['containerImage']}})
    else:
        return Response({"success": False,
            "message": "Invalid request data"})



# extract info from an image
@api_view(['POST'])
def extractInfo(request):
    extractedImagePath = str(settings.BASE_DIR)+str("/media/images/extractedImages/")
    fileName = str(uuid.uuid4())
    serializer = HiddenInfoContainerSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
    
        hiddenInfoContainerImage = open(str(settings.BASE_DIR)+ str(serializer.data['hiddenInfoContainerImage']), 'rb')

        content = hiddenInfoContainerImage.read()
        offset = content.index(bytes.fromhex("FFD9"))
        hiddenInfoContainerImage.seek(offset + 2)

        readInfo = hiddenInfoContainerImage.read()

        try:
            return Response({"success": True, "message": "Info extracted successfully","type":"TEXT", "body": {"textInfo": readInfo.decode()}})
        except:
            try:
                extractedImageInfo = Image.open(io.BytesIO(readInfo))
        
                extractedImageInfo.save(extractedImagePath+fileName+".jpg")
                imagePath = str("/media/images/extractedImages/")+fileName+".jpg"
                return Response({"success": True, "message": "Info extracted successfully","type":"IMAGE", "body": {"imagePath": imagePath}})
            except:
                try:
                    execpath = "/media/files/extractedExecFiles/"+fileName+".exe"
                    with open(str(settings.BASE_DIR) +execpath, "wb") as exec:
                        exec.write(readInfo)
                    return Response({"success": True, "message": "Info extracted successfully","type":"EXEC", "body": {"execPath": execpath}})

                except:
                    return Response({"success": False,
                "message": "Error Occured while extracting"})

    else:
        return Response({"success": False,
            "message": "Invalid request data"})






# @api_view(['POST'])
# def decryptMessage(request):
#     decryptedImagePath = str(settings.BASE_DIR)+str("/media/images/decrypted/"+"decryptedImage.jpg")
#     serializer = EncryptedMessageSerializer(data=request.data)

#     if serializer.is_valid(raise_exception=True):
#         serializer.save()

#     encryptedImage = open(str(settings.BASE_DIR) +
#                           str(serializer.data['encryptedImage']), 'rb')
#     content = encryptedImage.read()
#     offset = content.index(bytes.fromhex("FFD9"))
#     encryptedImage.seek(offset+2)

#     readInfo = encryptedImage.read()
#     decryptedImage = Image.open(io.BytesIO(readInfo))
#     decryptedImage.save(decryptedImagePath)

#     decryptedImageFile = Image.open(decryptedImagePath, 'r')
#     decryptedMessage = DecryptedMessage()
#     img_io = io.BytesIO()
#     img_ext = list(os.path.splitext(decryptedImageFile.filename))[-1]
#     decryptedImageFile.save(img_io, format="JPEG")
#     print(decryptedImageFile.filename)
#     decryptedMessage.decryptedImage = InMemoryUploadedFile(img_io,
#                                                       'ImageField',
#                                                       'decrypted'+ img_ext,
#                                                       'JPEG',
#                                                       sys.getsizeof(img_io), None)

#     decryptedMessage.save()

#     decryptedMessageObject = DecryptedMessage.objects.get(id=decryptedMessage.id)
#     decryptedMessageSerializer = DecryptedMessageSerializer(decryptedMessageObject, many=False)


#     return Response(decryptedMessageSerializer.data)




# @api_view(['POST'])
# def encryptMessage(request):
#     serializer = MessageSerializer(data=request.data)

#     if serializer.is_valid():
#         serializer.save()
#         print(serializer.data['textMsg'].encode())
#         imageFile = open(str(settings.BASE_DIR) +
#                          str(serializer.data['image1']), 'ab')
#         if serializer.data['image2'] != None:
#             img = Image.open(str(settings.BASE_DIR) + str(serializer.data['image2']))
#             byte_array = io.BytesIO()
#             img.save(byte_array, format='PNG')

#             imageFile.write(byte_array.getvalue())
#         elif serializer.data['textMsg'] != None:
#             imageFile.write(serializer.data['textMsg'].encode())
#         else:
#             return Response({"success": False, "message": "Invalid request body", "error": "error occured"})

#         imageFile.close()

#         return Response({"success": True,
#             "message": "Information Encrypted Successfully",
#             "body": serializer.data})

#     return Response("Invalid")

