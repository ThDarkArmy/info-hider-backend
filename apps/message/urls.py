from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('all/', views.getAll, name='Get All messages'),
    path('byId/<int:pk>/', views.getById, name='Get message by id'),
    path('encrypt/', views.encryptMessage, name='Encrypt Message'),
    path('decrypt/', views.decryptMessage, name='Decrypt Message')
]
