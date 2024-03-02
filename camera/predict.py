#### savefile에서 불러온 데이터를 기반으로 얼굴 예측하고 저장하는 실행파일 ####


from facenet import *
from savefile import *
import sys

if __name__ == "__main__":

    # 디렉토리 경로 설정(finalsite/camera/)
    # directory_path = '../faces'
    directory_path = 'static/assets/DB_img/verification'

    # main 함수 호출
    main(directory_path)


