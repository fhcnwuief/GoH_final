from django.urls import path

from . import views

urlpatterns = [
    path('',views.main, name='main'),
    path('emoji/',views.emoji, name = "emoji"),
    path('get_latest_data/', views.get_latest_data, name='get_latest_data')
]
