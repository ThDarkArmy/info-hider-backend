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
