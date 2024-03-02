import os
from django.conf import settings
from django.shortcuts import render,redirect
import pymysql
# 파일 저장 경로 생성 + sql 거주자 정보 등록
def get_connection():
    return pymysql.connect(
        host='192.168.90.73',
        user='guestuser',
        password='asdf1234!',
        database='project',
        cursorclass=pymysql.cursors.DictCursor
    )


def main(request):
    if request.method == 'POST':
        userid = request.POST.get('username', '')
        if userid:
            # 절대 경로로 디렉토리 경로 구성
            dir_path = os.path.join(settings.BASE_DIR, 'static/user_info', userid)
            base_path = os.path.relpath(dir_path,settings.BASE_DIR)

            # 디렉토리가 존재하지 않으면 생성
            if not os.path.exists(dir_path):
                os.makedirs(dir_path)
                print(f"Directory '{dir_path}' created successfully.")
                connection = get_connection()
                with connection.cursor() as cursor:
                    # sql에도 사용자 정보 생성
                    sql = "INSERT INTO resident (name,image_path) VALUES (%s,%s)"
                    cursor.execute(sql, (userid,base_path))
                    connection.commit()

                return redirect('/photo')
            else:
                print(f"Directory '{dir_path}' already exists.")

    return render(request,'new_user.html')
