from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators import gzip
from django.http import StreamingHttpResponse
from yolov5.models.experimental import attempt_load
from yolov5.utils.general import non_max_suppression
from yolov5.utils.torch_utils import select_device
from django.conf import settings
import cv2
import threading
import torch
import os
import datetime
import logging
from django.http import JsonResponse
import subprocess



def video(request):
    return render(request, 'page_video.html')


@gzip.gzip_page
def Home(request):
    try:
        cam = VideoCamera()
        return StreamingHttpResponse(
            gen(cam), content_type="multipart/x-mixed-replace;boundary=frame"
        )
    except Exception as e:
        print(f"Error in Home view: {e}")
    return render(request, "camera.html")

# YOLOv5 모델 초기화
model = None
device = None



def initialize_yolov5_model():
    global model, device
    weights_path = "./model_facenet/yolov5s.pt"  # 모델 가중치 경로
    device = select_device("cpu")  # GPU 또는 CPU 선택
    model = attempt_load(weights_path)
    model.to(device)
    model.eval()


# 카메라 캡처
class VideoCamera(object):
    def __init__(self):
        self.video = cv2.VideoCapture(0)
        (self.grabbed, self.frame) = self.video.read()
        self.capture_count = 0  # 객체 감지 횟수 카운트 변수
        threading.Thread(target=self.update, args=()).start()

    def __del__(self):
        self.video.release()

    def get_frame(self):
        # 좌우 반전 적용
        image = cv2.flip(self.frame, 1)
        # YOLOv5를 사용한 객체 검출
        result_image = detect_objects(image)
        # 순간순간 이미지를 encode하여 보여줌
        _, jpeg = cv2.imencode(".jpg", result_image)
        # 200번 객체를 감지하면 전체 화면 캡처
        self.capture_count += 1
        if self.capture_count >= 200:
            capture_full_screen(result_image)
            logging.info(f"capture_count: {self.capture_count}")  # 로그에 출력
            self.capture_count = 0  # 초기화
            
        return jpeg.tobytes()

    def update(self):
        while True:
            (self.grabbed, self.frame) = self.video.read()

# 사람 객체 검출
def detect_objects(frame):
    #########################<MAC>#########################
    # Resize the frame to the desired size (480x640)
    target_height, target_width = 480, 640
    frame = cv2.resize(frame, (target_width, target_height))
    ########################################################
    img = frame
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img = torch.from_numpy(img).to(device)
    img = img.float()  # 정확한 숫자 값으로 변환
    img /= 255.0  # 0-255 범위를 0-1로 조정

    img = img.permute(2, 0, 1)
    # YOLOv5 객체 검출 수행
    img = img.unsqueeze(0)  # 배치 차원 추가
    pred = model(img)[0]

    # 결과 후처리
    pred = non_max_suppression(pred, 0.4, 0.5)[0]  # 임계값 및 NMS 적용

    # 바운딩 박스 그리기
    result_image = frame.copy()
    detected_objects = []

    for det in pred:
        if det[-1] == 0:
            x1, y1, x2, y2, conf = det[:5]
            x1, y1, x2, y2 = map(int, (x1, y1, x2, y2))
            # cv2.rectangle(result_image, (x1, y1), (x2, y2), (0, 255, 0), 2)
            cv2.rectangle(result_image, (x1, y1), (x2, y2), (0, 0, 0), 0)

            # 이미지 저장 경로 및 파일명 지정
            BASE_DIR = settings.BASE_DIR
            image_path = os.path.join(BASE_DIR, "static/assets/DB_img/captured_images","object_detection.jpg")
            
            # 잘라낸 이미지를 저장
            cv2.imwrite(image_path, frame)
            detected_objects.append(frame)
            
    return result_image

# 전체 화면 캡처
def capture_full_screen(image):
    
    # 현재 날짜 및 시간을 포맷에 맞춰 문자열로 가져오기
    current_time = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    # 파일명에 현재 시간 추가
    filename = f"{current_time}.jpg"
    # image_path = os.path.join(settings.BASE_DIR, "camera/faces", filename)
    image_path = os.path.join(settings.BASE_DIR, "static/assets/DB_img/verification", filename)
    cv2.imwrite(image_path, image)


def gen(camera):
    while True:
        frame = camera.get_frame()
        yield (b"--frame\r\n" b"Content-Type: image/jpeg\r\n\r\n" + frame + b"\r\n\r\n")



# YOLOv5 모델 초기화
initialize_yolov5_model()
# ======================화면녹화부분=====================

def save_video(request):
    if request.method == 'POST' and request.FILES.get('video'):
        video = request.FILES['video']
        with open(f'static/assets/DB_img/video/{video.name}', 'wb') as f:
            for chunk in video.chunks():
                f.write(chunk)

        return JsonResponse({'success': True})

    return JsonResponse({'success': False})

def start_recording(request):
    try:
        # Implement camera recording logic here (adjust the command as needed)
        video_filename = f'static/assets/DB_img/video/{datetime.datetime.now().strftime("%Y%M%D_%H%M%S")}.mp4'
        os.makedirs(os.path.dirname(video_filename), exist_ok=True)
        logging.info(f"Attempting to access or create file: {video_filename}")
        subprocess.run(['ffmpeg', '-i', 'http://127.0.0.1:8000/video/camera/', '-r', '60', '-t', '5', '-c:v', 'libx264', video_filename])
        # subprocess.run(['ffmpeg', '-i', 'http://192.168.80.14:8000/video/camera/', '-r', '60', '-t', '5', '-c:v', 'libx264', video_filename])

        return JsonResponse({'success': True, 'video_filename': video_filename})
    except Exception as e:
        print(f"Error starting recording: {e}")
        return JsonResponse({'success': False, 'error': str(e)})

# http://192.168.80.14:8000/video/camera/
# http://127.0.0.1:8000/video/camera/


