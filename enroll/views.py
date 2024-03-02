from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import PhotoForm
import pymysql
import base64
from django.shortcuts import render
from django.views.decorators.csrf import ensure_csrf_cookie
from django.http import JsonResponse
from django.conf import settings
import os

def get_connection():
    return pymysql.connect(
        host='localhost',
        user='root',
        password='wlsdud1004',
        database='project',
        cursorclass=pymysql.cursors.DictCursor
    )

def get_user_name():
    connection = get_connection()
    with connection.cursor() as cursor:
        sql = "SELECT name FROM resident"
        cursor.execute(sql)

        datas = cursor.fetchall()

    name_values = []

    for entry in datas:
        name_values.append(entry['name'])
    print('name_values:',name_values)
    return name_values

def get_first_image_name(base_folder_path):
    items = [item for item in os.listdir(base_folder_path)]

    first_file_path = os.path.join(base_folder_path,items[0]).replace('\\','/')

    return first_file_path

def main(request):
    first_image_name = []
    user = get_user_name()
    # 각 user에 대해 base_folder_path 생성 및 처리
    for single_user in user:
        base_folder_path = f'static/user_info/{single_user}'
        first_image_names = get_first_image_name(base_folder_path)
        first_image_names = first_image_names.replace('static/user_info/','')
        print(first_image_names)
        first_image_name.append(first_image_names)
    print('first_image_name : ',first_image_name)
    return render(request, 'enroll.html', {'first_image_names': first_image_name,'user':user})