from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import PhotoForm
from django.conf import settings
import pymysql
from PIL import Image
import base64
from io import BytesIO
import os
import shutil

def main(request):
    return render(request, 'page_photo.html')


def get_connection():
    return pymysql.connect(
        host='localhost',
        user='root',
        password='wlsdud1004',
        database='project',
        cursorclass=pymysql.cursors.DictCursor
    )

def upload_photo(request):
    if request.method == 'POST':
        form = PhotoForm(request.POST, request.FILES)
        if form.is_valid():
            # 파일이름들을 담을 리스트 초기화
            uploaded_file_names = []
            # form을 통해 업로드된 파일들의 리스트를 받아옴
            images = request.FILES.getlist('image')
            for uploaded_file in images:
                # 각 파일의 이름을 리스트에 추가
                uploaded_file_names.append(uploaded_file.name)

            move_file(uploaded_file_names)
            connection = get_connection()
            try:
                with connection.cursor() as cursor:
                    for image in images:
                        # 이미지를 데이터베이스에 저장
                        sql = '''
                                UPDATE resident
                                SET image_data = %s
                                WHERE id = 1
                            '''
                        cursor.execute(sql, (image.read(),))
                        connection.commit()

                        sql = "INSERT INTO images (image) VALUES (%s)"
                        cursor.execute(sql, (image.read(),))
                        connection.commit()

                    image_list = display_photos()

            finally:
                connection.close()
            return render(request, 'page_photo_sub1.html',{'image_list':image_list})
    else:
        form = PhotoForm()
    return render(request, 'page_photo.html', {'form': form})

def move_file(list):
    connection = get_connection()
    with connection.cursor() as cursor:
        sql = '''
                SELECT name FROM resident
                WHERE name = %s'''

        cursor.execute(sql)
        datas = cursor.fetchall()

    for file_name in list:
        print(file_name)
        # 원본 파일 경로
        # local 경로에서 가져오고 싶었으나 그것은 나중 문제
        # 다른 파이썬 어플들과 같은 경로에 존재하다, static안
        # 사용자 파일 경로로 들어가는 코드로 우선 구현
        absolute_path = os.path.abspath(file_name).replace("\\", "/")
        script_directory = os.path.dirname(os.path.abspath(__file__))
        print('script_directory',script_directory)
        print('absolute_path',absolute_path)
        # 목적지 경로
        new_file = 'static/user_info/' + str(datas[0]['name'])+'/'
        file_path = new_file + file_name
        print('new_file',new_file)
        new_path = os.path.abspath(file_path).replace("\\", "/")
        print('new_path',new_path)
        shutil.copy2(absolute_path, new_path)
        print("file copied")



def display_photos():
    connection = get_connection()
    try:
        with connection.cursor() as cursor:
            sql = "SELECT image FROM images"
            cursor.execute(sql)
            photos = cursor.fetchall()
    finally:
        connection.close()

    image_list = []
    for photo in photos:
        image_data = photo.get('image')
        if image_data:
            encoded_image_data = base64.b64encode(image_data).decode('utf-8')
            image_list.append(encoded_image_data)

    return image_list
