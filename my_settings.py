# SQLite3 -> MySQL
# settings.py 수정
DATABASES = {
    "default": {
        # 사용할 엔진 설정
        "ENGINE": "django.db.backends.mysql",
        # 연동할 MySQL의 데이터베이스 이름
        "NAME": "project",
        # 계정명이랑 비밀번호는 미주만 root
        # 나머지 분들은 사용하실때
        # 계정명 : guestuser
        # pw : asdf1234! 로 수정하셔야 할걸요?
        # 접속 ip는 사용할때 미주한테 물어보셔요
        # DB 접속 계정명
        "USER": "root",
        # 해당 DB 접속 계정 비밀번호
        "PASSWORD": "wlsdud1004",
        # 실제 DB 주소
        "HOST": "localhost",
        # 포트 번호
        "PORT": "3306",
    }
}
SECRET_KEY = 'django-insecure-!4^dxe-2ba=g^sdedsx6gk4@zl*ddt@a9s#waq@x2!0y*mhi_u'