from django.urls import path

from . import views

urlpatterns = [
    path('',views.main, name='photo'),
    path('upload/', views.upload_photo, name='upload_photo'),
    path('display/', views.display_photos, name='display_photos'),
]
