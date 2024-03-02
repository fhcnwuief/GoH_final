from django.urls import path

from . import views


urlpatterns = [
    path('',views.main, name='detect_sub1'),
    #path('/imageSrc=%s/newImageUrl=%s', views.img_path, name='img_path'),
    path('person1/',views.img_path1,name='person1'),
    path('person2/',views.img_path2,name='person2'),
    path('person3/',views.img_path3,name='person3'),
    path('person4/',views.img_path4,name='person4'),
    path('complete/',views.complete,name='complete'),
]
