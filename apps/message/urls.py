from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('all/', views.getAll, name='Get All messages'),
    path('byId/<int:pk>/', views.getById, name='Get message by id'),
    path('create/', views.createEncryptedMessage, name='create encryptedMessage'),
    # path('update/<int:pk>/', views.updateUser, name='update user'),
    # path('delete/<int:pk>/', views.deleteUser, name='delete user')

]
