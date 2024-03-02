from django.contrib import admin
from django.urls import path,include
from login_out.views import * 
from main.views import *
from history.views import *

urlpatterns = [
    # 관리자 페이지
    path('admin/', admin.site.urls),
    # 첫 페이지
    # 로그인/회원가입 페이지
    path('', login_view, name="login"),
    path('login/',include('login_out.urls')),    
    # mainpage 
    path('main/', main, name='main'),
    path('',include('main.urls')),
    # 카메라 on -> 얘한테 yolo
    path('video/',include('camera.urls')),      
    # mail 기능
    path('mail/',include('mail.urls')),
    # 거주자1정보 page
    path('user1/', include('user1.urls')),
    # 추가등록 Page
    path('enroll/', include('enroll.urls')),
    # 신규거주자 등록 page
    path('new_user/', include('new_user.urls')),
    # 문자내용 page
    path('sent_list/', include('sent_list.urls')),
    # 사진등록 page
    path('photo/', include('page_photo.urls')),
    # 상세 프로필 page
    path('profile/', include('page_profile.urls')),
    # 전체이력조회
    path('history/', history, name='history'),
    path('', include('history.urls')),
    # 최근 감지 이력 page
    path('detect_main/', include('page_detect.urls')),
    # 최근 감지 이력 page -sub1
    path('detect_sub1/', include('page_detect_sub1.urls')),
    # 최근 감지 이력 page - sub2
    path('detect_sub2/', include('page_detect_sub2.urls')),
    # 최근 감지 이력 page - sub3
    path('detect_sub3/', include('page_detect_sub3.urls')),
    # pin apge
    path('pin/', include('sos_pin.urls'))
]
