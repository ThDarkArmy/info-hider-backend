from django.urls import path
from . import views

urlpatterns = [
    # path('all/', views.getAll, name='Get All messages'),
    # path('byId/<int:pk>/', views.getById, name='Get message by id'),
    # path('encrypt/', views.encryptMessage, name='Encrypt Message'),
    # path('decrypt/', views.decryptMessage, name='Decrypt Message'),
    path('hide-text', views.hideText, name="Hide Text"),
    path('hide-image', views.hideImage, name="Hide Image"),
    path('hide-exec', views.hideExec, name="Hide Exec"),
    path('extract-info', views.extractInfo, name="Extract info from container")
]
