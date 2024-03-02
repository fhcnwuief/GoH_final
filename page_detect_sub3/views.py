from django.shortcuts import render
import pymysql
def main(request):
    with pymysql.connect(host='192.168.90.73', user='guestuser', password='asdf1234!', db='project',
                             charset='utf8') as connection:
        cursor = connection.cursor(pymysql.cursors.DictCursor)

        SQL = '''
                    SELECT path,create_at
                    FROM project.`unknown`
                    WHERE result = %s
                    ORDER BY create_at DESC
                    LIMIT 1;
                '''

        param = "unknown"
        cursor.execute(SQL, param)

        datas = cursor.fetchall()

        print('detect_views: ', datas)

    return render(request, 'detect_sub3.html', {'images': datas})