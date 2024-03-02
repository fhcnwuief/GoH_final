#### mysql에 저장된 데이터 불러온 후 인증한 데이터 DB에 저장 ####

import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "GoH.settings")
import pymysql
import os
import datetime
import time
import subprocess
import cv2
from facenet import *



def main(directory_path):

    # 최초 파일 경로 가져오기
    previous_file_path = os.listdir(directory_path)
    print('previous_file_path: ', previous_file_path)
    # 파일명을 최근 수정된 순서로 정렬
    previous_file_path.sort(key=lambda x: os.path.getctime(os.path.join(directory_path, x)) if x != '.DS_Store' else float('-inf'))
    # 가장 최근에 생성된 파일의 경로 반환
    image_file_path = os.path.join(directory_path, previous_file_path[-1])
    print('savefile, 최초생성파일경로: ', image_file_path)

    while True:
        # 최근 파일 가져오기
        latest_file_path = os.listdir(directory_path)
        # 파일명을 최근 수정된 순서로 정렬
        latest_file_path.sort(key=lambda x: os.path.getmtime(os.path.join(directory_path, x)) if x != '.DS_Store' else float('-inf'))
        # 가장 최근에 생성된 파일의 경로 반환
        latest_file_path = os.path.join(directory_path, latest_file_path[-1])
        print('savefile, 새로 가져온 파일경로: ', latest_file_path)

        # 새로운 파일이 있는지 확인
        if image_file_path != latest_file_path:
            print(f"savefile, 진짜 새로 생성된 파일: {latest_file_path}")
            
            # 새로운 얼굴 예측 시작
            predicted_names = load_and_predict_new_image(latest_file_path)   
            print("savefile, Predicted Names:", predicted_names)
            
            # 데이터베이스에 예상 이름 삽입
            relative_path = os.path.relpath(latest_file_path, start="static")
            print('savefile, DB저장경로: ', relative_path)
            insert_predicted_names(predicted_names, relative_path)

            # 현재 파일 경로를 저장
            image_file_path = latest_file_path
            print('savefile, imgage_file_path:', image_file_path)
        else:
            pass
        # 10초마다 확인
        time.sleep(10)
        
        

# 이미지에서 얻은 예상 이름을 데이터베이스에 삽입
def insert_predicted_names(predicted_names, relative_path):
    # MySQL 연결 정보
    db_config = db_config = {
        'host': 'localhost',
        'user': 'root',
        'password': 'wlsdud1004',
        'database': 'project',  # 데이터베이스 이름으로 변경해야 합니다.
        'port': 3306,
        'charset': 'utf8'
    }

    conn = None
    cursor = None

    try:
        # MySQL 연결
        conn = pymysql.connect(**db_config)
        cursor = conn.cursor()

        # 예상 이름을 predicted_names 테이블에 삽입
        for name in [predicted_names]:
            print(f"Inserting into result table: {name}")
            cursor.execute('''
                INSERT INTO project.result(result, path)
                SELECT %s, %s
                FROM dual
                WHERE NOT EXISTS (
                    SELECT *
                    FROM project.result
                    WHERE path = %s
                )
            ''', (name, relative_path, relative_path))
            # If the result is "unknown", also insert into project.unknown table
            if name == "unknown":
                print(f"Inserting into unknown table: {name}")
                cursor.execute('''
                    INSERT INTO project.unknown(result, path)
                    SELECT %s, %s
                    FROM dual
                    WHERE NOT EXISTS (
                        SELECT *
                        FROM project.unknown
                        WHERE path = %s
                    )
                ''', (name, relative_path, relative_path))

        # 변경 내용을 커밋
        conn.commit()
 
    except Exception as e:
        print(f"Error: {e}")

    finally:
        # 연결 종료
        if cursor:
            cursor.close()
        if conn:
            conn.close()
            
