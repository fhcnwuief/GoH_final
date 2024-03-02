from django.shortcuts import render,redirect
import pymysql
from django.conf import settings


def main(request):
    with pymysql.connect(host='192.168.90.73', user='guestuser', password='asdf1234!', db='project',charset='utf8') as connection:
        cursor = connection.cursor(pymysql.cursors.DictCursor)

        SQL = '''
                SELECT path,create_at
                FROM project.`unknown`
                WHERE result = %s
                ORDER BY create_at DESC
                LIMIT 1;
            '''

        param = "unknown"
        cursor.execute(SQL,param)

        datas = cursor.fetchall()

        print('detect_sub1_view: ',datas)

    return render(request, 'detect_sub2.html', {'images': datas})

def insert_mail_img(path,create,result):

    with pymysql.connect(host='192.168.90.73', user='guestuser', password='asdf1234!', db='project',charset='utf8') as connection:
        cursor = connection.cursor(pymysql.cursors.DictCursor)
        sql = '''
                INSERT INTO mail_img (path, create_at, result)
                VALUES (%s, %s, %s);
            '''

        values = (path, create, result)
        cursor.execute(sql, values)

        connection.commit()


def save_info(request):
    with pymysql.connect(host='192.168.90.73', user='guestuser', password='asdf1234!', db='project',charset='utf8') as connection:
        cursor = connection.cursor(pymysql.cursors.DictCursor)

        SQL = '''
                SELECT path, create_at, result
                FROM project.`unknown`
                WHERE result = %s
                ORDER BY create_at ASC
                LIMIT 1;
            '''

        param = "unknown"
        cursor.execute(SQL, param)

        datas = cursor.fetchall()

        path = datas[0]['path']
        create = datas[0]['create_at']
        result = datas[0]['result']
        print('detect_sub1_view: ', path,create,result)
        insert_mail_img(path,create,result)

    return redirect('mail')

