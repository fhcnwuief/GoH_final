from django.urls import path

from . import views

urlpatterns = [
    # path('',views.index),
    path('',views.mail, name='mail'),
    path('sendmail/', views.sendmail, name='sendmail'),
    path('check/',views.check,name='check')
]
