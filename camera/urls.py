from django.urls import path
from . import views

urlpatterns = [
    path('camera/',views.Home, name='camera_ori'),     # original camera page
    path('', views.video, name='video'),               # resize camera page
    path('start-recording/', views.start_recording, name='start_recording'),

]