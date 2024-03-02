from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import pymysql
from django.shortcuts import render,redirect
from django.conf import settings



def main(request):
    with pymysql.connect(user='root', password='wlsdud1004', host='localhost', port=3306, charset='utf8') as connection:
        cursor = connection.cursor(pymysql.cursors.DictCursor)

        SQL = '''
            SELECT COUNT(*)
            FROM project.`unknown`
            WHERE result = %s;
        '''

        param = "unknown"
        cursor.execute(SQL, param)
        result_count = cursor.fetchone()
        count_value = int(result_count.get('COUNT(*)', 0))
        print(count_value)

        if count_value == 3:

            SQL = '''
                    INSERT INTO project.`unknown` (path, result, create_at)
                    SELECT path, result, create_at
                    FROM project.result
                    WHERE result = %s;
                '''
            cursor.execute(SQL, param)
            connection.commit()

        SQL = '''
                SELECT path
                FROM project.`unknown`
                ORDER BY create_at DESC
                LIMIT 0,3;
            '''

        cursor.execute(SQL)

        datas = cursor.fetchall()
        print(datas)

        SQL =  '''
            SELECT home FROM project.user
            '''

        cursor.execute(SQL)
        address = cursor.fetchall()
        print(address[0]['home'])
        gu_name = str(address[0]['home']).split(' ')[0]
        print(gu_name)
        SQL = '''
                SELECT * FROM project.research
                WHERE gu_name = %s
            '''
        param = gu_name
        cursor.execute(SQL, param)

        research = cursor.fetchall()

        print(research)

    return render(request, 'page_main.html', {'images': datas ,'data':research})

previous_data = None

@csrf_exempt
def get_latest_data(request):
    global previous_data

    # Establish a connection to the MySQL database
    connection = pymysql.connect(user='root', password='wlsdud1004!', host='localhost', port=3306, charset='utf8')

    try:
        with connection.cursor() as cursor:
            # Your SQL query to fetch data from the database
            query = "SELECT * FROM project.result ORDER BY id DESC LIMIT 1"
            cursor.execute(query)
            
            verification_data = cursor.fetchone()
            print('main_view, 인증데이터: ', verification_data)
            verification_name = verification_data[1]
            current_data = verification_data[3]
            print('main_view, 현재 데이터: ', current_data)

        # Compare data and send notification if different
        if previous_data is not None and current_data != previous_data:
            notification_data = {
                'message': verification_name + '인증되었습니다.',
                'current_data': verification_name
            }
            print('main_view: ', notification_data)
        # Update the verification_name or perform other actions as needed
            verification_name = 'code_for_popup_notification'
        else:
            notification_data = None

        # Update the previous data
        previous_data = current_data
        print('main_view, 바뀐 이전데이터: ', previous_data)

    finally:
        connection.close()

    return JsonResponse(notification_data, safe=False)


def emoji(request):
    with pymysql.connect(user='guestuser', password='asdf1234!', host='192.168.90.73', port=3306, charset='utf8') as connection:
        cursor = connection.cursor(pymysql.cursors.DictCursor)

        SQL = '''
                SELECT * FROM project.research
            '''

        param = "서초구"
        cursor.execute(SQL,param)

        datas = cursor.fetchall()

        print(datas)

    return render(request, 'page_main.html', {'data': datas})
