from django.shortcuts import render, redirect
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.http import HttpResponse
import pymysql

def mail(request):
    with pymysql.connect(host='localhost', user='root', password='wlsdud1004', db='project',charset='utf8') as connection:
        cursor = connection.cursor(pymysql.cursors.DictCursor)

        SQL = '''
                SELECT user.* , message.text, mail_img.result, mail_img.*
                FROM project.`user`,project.`message`,project.`mail_img`
                WHERE user.id = message.id AND message.id = mail_img.id
            '''

        cursor.execute(SQL)
        datas = cursor.fetchall()
        print(datas)
    return render(request, 'mail.html', {'texts': datas})


def sendmail(request):
    if request.method == 'POST':
        recipient = request.POST.get('email')
        subject = request.POST.get('subject')
        name = request.POST.get('name')
        message = request.POST.get('message')
        from_email = 'gtoh.main@gmail.com'  # 이메일을 보내는 사람의 이메일 주소

        email = EmailMessage(subject, message, from_email, [recipient])
        email.content_subtype = "html"

        try:
            email.send()
            return HttpResponse("메일이 성공적으로 전송되었습니다.")
        except Exception as e:
            return HttpResponse("메일 전송 중 오류가 발생했습니다: " + str(e))
    return redirect('/')

def insert_sending(name, email):
    with pymysql.connect(host='localhost', user='root', password='wlsdud1004', db='project',charset='utf8') as connection:
        cursor = connection.cursor(pymysql.cursors.DictCursor)

        SQL = '''
            INSERT INTO project.`sending` (receive,e_mail)
            VALUES (%s,%s)
            '''

        values = (name,email)
        cursor.execute(SQL, values)

        connection.commit()

def check():
    with pymysql.connect(host='localhost', user='root', password='wlsdud1004', db='project',charset='utf8') as connection:
        cursor = connection.cursor(pymysql.cursors.DictCursor)


        SQL = '''
            SELECT name, email
            FROM user
            WHERE id = 1
            '''

        cursor.execute(SQL)

        datas = cursor.fetchall()

        name = datas[0]['name']
        email = datas[0]['email']
        print(name,email)
        insert_sending(name, email)