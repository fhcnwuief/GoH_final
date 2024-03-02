from django.shortcuts import render
import pymysql

def main(request):
    with pymysql.connect(host='192.168.90.73', user='guestuser', password='asdf1234!', db='project',charset='utf8') as connection:
        cursor = connection.cursor(pymysql.cursors.DictCursor)

        SQL = '''
                SELECT project.sending.*
                FROM project.sending
            '''

        cursor.execute(SQL)
        datas = cursor.fetchall()
        print(datas)

        if len(datas) > 20:
            excess_posts = datas[:len(datas) - 20]
            for excess_post in excess_posts:
                delete_sql = '''
                            DELETE FROM project.sending
                            WHERE id = %s
                            ORDER BY id
                            LIMIT 1                           
                        '''
                cursor.execute(delete_sql, excess_post['id'])
                connection.commit()


        cursor.execute(SQL)
        datas = cursor.fetchall()

    return render(request, 'sent_list.html', {'posts': datas})