import pymysql
import os
import json
from django.shortcuts import render,redirect
from django.http import HttpResponse
import logging
import shutil
import re


# DB에서 unknown으로 판단한 이미지 경로와 timastamp 추출
def database():
    with pymysql.connect(host='192.168.90.73', user='guestuser', password='asdf1234!', db='project',charset='utf8') as connection:
        cursor = connection.cursor(pymysql.cursors.DictCursor)

        SQL = '''
                SELECT path,create_at
                FROM project.`unknown`
                ORDER BY create_at DESC
                LIMIT 1;
            '''
        cursor.execute(SQL)

        datas = cursor.fetchall()

        print(datas)

    return datas


def imgpath():
    datas = database()
    images = [{item['path']} for item in datas]
    images = '/'.join(str(image) for image in images)
    file_path = re.search(r"'(.*?)'", images).group(1)
    changed_list = os.path.basename(file_path)
    image_list = 'static/assets/DB_img/verification/' + changed_list
    print('detect_sub1_view, image_list: ', image_list)
    abs_img_list = os.path.abspath(image_list)   # 옮길 폴더경로
    print('detect_sub1_view, abs_img_list: ', abs_img_list)
    return abs_img_list,changed_list


def main(request):
    datas = database()
    print('detect_sub1_view: ', datas)
    return render(request, 'detect_sub1.html', {'images': datas})


def img_path1(request):
    abs_img_list,changed_list = imgpath()
    # new_data = 'static/assets/DB_img/person1/' + changed_list
    new_data = 'camera/dataset/changhoon/' + changed_list   
    abs_new_data = os.path.abspath(new_data)
    print('detect_sub1_view: ', new_data)
    shutil.copy2(abs_img_list, abs_new_data)
    print("file copied")
    complete()

    return redirect('main')

def img_path2(request):
    abs_img_list, changed_list = imgpath()
    new_data = 'camera/dataset/koeun/' + changed_list
    abs_new_data = os.path.abspath(new_data)
    print('detect_sub1_view: ',new_data)
    shutil.copy2(abs_img_list, abs_new_data)
    print("detect_sub1_view, file copied")
    complete()

    return redirect('main')

def img_path3(request):
    abs_img_list, changed_list = imgpath()
    new_data = 'camera/dataset/mijoo/' + changed_list
    abs_new_data = os.path.abspath(new_data)
    print('detect_sub1_view: ',new_data)
    shutil.copy2(abs_img_list, abs_new_data)
    print("file copied")
    complete()

    return redirect('main')

def img_path4(request):
    abs_img_list, changed_list = imgpath()
    new_data = 'camera/dataset/subeen/' + changed_list
    abs_new_data = os.path.abspath(new_data)
    print('detect_sub1_view, ',new_data)
    shutil.copy2(abs_img_list, abs_new_data)
    print("file copied")
    complete()

    return redirect('main')

def complete():
    with pymysql.connect(host='192.168.90.73', user='guestuser', password='asdf1234!', db='project',charset='utf8') as connection:
        cursor = connection.cursor(pymysql.cursors.DictCursor)


        SQL = '''
                DELETE FROM project.`unknown`
                ORDER BY create_at DESC
                LIMIT 1;
                '''

        cursor.execute(SQL)
        connection.commit()





