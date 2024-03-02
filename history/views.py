from django.shortcuts import render
import pymysql
from django.http import JsonResponse
import os
from django.conf import settings


def history(request):
    return render(request, 'page_history.html')

def history_list(request):
    try:
        # MySQL 연결 정보
        db_config = {
            'host': 'localhost',
            'user': 'root',
            'password': 'wlsdud1004',
            'database': 'project',  # 데이터베이스 이름으로 변경해야 합니다.
            'port': 3306,
            'charset': 'utf8'
        }

        # Establish a connection
        conn = pymysql.connect(**db_config)
        cursor = conn.cursor(pymysql.cursors.DictCursor)

        # id값을 기준으로 최근 데이터 20개를 가져옴
        query = "SELECT * FROM project.result ORDER BY id  DESC LIMIT 20"
        cursor.execute(query)
        verified_results = cursor.fetchall()
        # print('인증정보 :', verified_results)

        card_list = []
        for verified_result in verified_results:
            print('history_main, Single Row:', verified_result)
            verified_name = 'admin' if verified_result['result'] != 'unknown' else 'unknown'
            data_time = verified_result['create_at']
            verified_time = data_time.strftime("%Y-%m-%d %H:%M:%S")
            # full_path= verified_result['path'].lstrip('.')
            verified_img= verified_result['path'].lstrip('.')
            # full_path= verified_result['path']
            print('history_main, full_path1:', verified_img)

            card = {
                'verified_name': verified_name,
                'verified_time': verified_time,
                'verified_img': verified_img
            }
            card_list.append(card)
            # print('card_list: ', card_list)

        # Close the database connection
        conn.close()

        # Return the JsonResponse with the card_list
        return JsonResponse(card_list, safe=False)

    except Exception as e:
        # Print the exception details
        print('Error:', e)
        import traceback
        traceback.print_exc()
        # Handle exceptions and return an error response
        error_data = {'error': 'Internal Server Error'}
        return JsonResponse(error_data, status=500)


    