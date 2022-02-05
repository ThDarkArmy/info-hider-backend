from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('all/', views.getAll, name='Get All users'),
    path('byId/<int:pk>/', views.getById, name='Get user by id'),
    path('create/', views.createUser, name='create user'),
    path('update/<int:pk>/', views.updateUser, name='update user'),
    path('delete/<int:pk>/', views.deleteUser, name='delete user')

]



# img = Image.open(str(settings.BASE_DIR) +str(serializer.data['image1']))
        # img_ext = list(os.path.splitext(img.filename))[-1]
        # img_io = io.BytesIO()
        # img.save(img_io, format="JPEG")
        # new_pic= InMemoryUploadedFile(img_io, 
        #     'ImageField',
        #     'profile_pic'+img_ext,
        #     'JPEG',
        #     sys.getsizeof(img_io), None)

        # encryptedMessage.image = new_pic
        
        # encryptedMessage.image.save('images', open(str(settings.BASE_DIR) +str(serializer.data['image1']), 'rb'))
        # encryptedMessage.image = str(serializer.data['image1'])

        # print("Encrypted Message", serialize('json', [encryptedMessage]))

        # print(encryptedMessage.image)
        # print(new_pic)

        # msg = serialize('json', [encryptedMessage])
