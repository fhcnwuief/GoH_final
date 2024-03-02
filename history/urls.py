from django.urls import path

from . import views

urlpatterns = [
    path('history_list/',views.history_list, name='history_list')
    
]
