import pymysql

conn = pymysql.connect(user='root', password='wlsdud1004', host='localhost', db='project', charset='utf8')
cursor = conn.cursor(pymysql.cursors.DictCursor)

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
    conn.commit()

SQL = '''
        SELECT path
        FROM project.`unknown`
        ORDER BY create_at DESC
        LIMIT 0,3;
    '''

cursor.execute(SQL)

datas = cursor.fetchall()
print('데이터: ', datas)

SQL =  '''
    SELECT home FROM user
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