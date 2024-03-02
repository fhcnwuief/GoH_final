from django.urls import path

from . import views

urlpatterns = [
    path('',views.main, name='detect_sub2'),
    path('save_info/',views.save_info,name = 'save_info')
]
