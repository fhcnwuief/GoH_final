#### 카메라 기능 관련 파일 ####


import cv2 as cv
import os
import numpy as np
import tensorflow as tf
import pickle
import matplotlib.pyplot as plt
from mtcnn.mtcnn import MTCNN
from keras_facenet import FaceNet
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC




class FaceLoader:
    def __init__(self, directory):
        print(directory)
        self.directory = directory
        self.target_size = (160, 160)
        self.X = []
        self.Y = []
        self.detector = MTCNN()

    def extract_face(self, filename):
        img = cv.imread(filename)
        img = cv.cvtColor(img, cv.COLOR_BGR2RGB)
        x, y, w, h = self.detector.detect_faces(img)[0]["box"]
        x, y = abs(x), abs(y)
        face = img[y : y + h, x : x + w]
        face_arr = cv.resize(face, self.target_size)
        return face_arr

    def load_faces(self, dir):
        FACES = []
        for im_name in os.listdir(dir):
            try:
                path = dir + im_name
                single_face = self.extract_face(path)
                FACES.append(single_face)
            except Exception as e:
                pass
        return FACES

    def load_classes(self):
        for sub_dir in os.listdir(self.directory):
            path = self.directory + "/" + sub_dir + "/"
            FACES = self.load_faces(path)
            labels = [sub_dir for _ in range(len(FACES))]
            print(f"Loaded successfully: {len(labels)}")
            self.X.extend(FACES)
            self.Y.extend(labels)
        return np.asarray(self.X), np.asarray(self.Y)


def get_embedding(face_img):
    # Facenet part
    embedder = FaceNet()
    face_img = face_img.astype("float32")
    face_img = np.expand_dims(face_img, axis=0)
    yhat = embedder.embeddings(face_img)
    return yhat[0]


# Declare encoder as a global variable
encoder = LabelEncoder()


def train_and_save_model():
    os.environ["TF_CPP_MIN_LOG_LEVEL"] = "2"

    # Load faces and embeddings
    faceloader = FaceLoader("camera/dataset")
    X, Y = faceloader.load_classes()

    EMBEDDED_X = [get_embedding(img) for img in X]
    EMBEDDED_X = np.asarray(EMBEDDED_X)
    np.savez_compressed("faces_embeddings_done.npz", EMBEDDED_X, Y)

    # Fit the encoder
    global encoder
    encoder.fit(Y)
    Y = encoder.transform(Y)

    X_train, X_test, Y_train, Y_test = train_test_split(
        EMBEDDED_X, Y, shuffle=True, random_state=17
    )

    model = SVC(kernel="linear", probability=True)
    model.fit(X_train, Y_train)
    
    # Get the current script directory
    script_directory = os.path.dirname(os.path.abspath(__file__))
    model_file_path = os.path.join(script_directory, "model_facenet", "svm_model_160x160.pkl")
    encoder_file_path = os.path.join(script_directory, "model_facenet", "label_encoder.pkl")
    
        # Use the absolute path
    with open(model_file_path, "wb") as f:
        pickle.dump(model, f)
    with open(encoder_file_path, "wb") as f:
        pickle.dump(encoder, f)
        


def load_and_predict_new_image(latest_file_path):
    # Get the current script directory
    # base_directory =/Users/rachel/PlayData/finalproject4/finalsite/camera
    base_directory = os.path.dirname(os.path.abspath(__file__))

    # Construct the absolute path to the model file
    model_file_path = os.path.join(base_directory, "model_facenet", "svm_model_160x160.pkl")
    encoder_file_path = os.path.join(base_directory, "model_facenet", "label_encoder.pkl")

    # Use the absolute path
    with open(model_file_path, "rb") as f:
        model = pickle.load(f)
    with open(encoder_file_path, "rb") as f:
        encoder = pickle.load(f)

    # Image preprocessing
    detector = MTCNN()
    t_im = cv.imread(latest_file_path)
    t_im = cv.cvtColor(t_im, cv.COLOR_BGR2RGB)
    
    # Detect faces
    faces = detector.detect_faces(t_im)
    if not faces:
        print("Error: No face detected.")
        return "Unknown"
    else:
        x, y, w, h = detector.detect_faces(t_im)[0]["box"]
        t_im = t_im[y : y + h, x : x + w]
        t_im = cv.resize(t_im, (160, 160))
        test_im = get_embedding(t_im)

        test_im = [test_im]
        ypreds = model.predict(test_im)
        predicted_names = encoder.inverse_transform(ypreds)

        return predicted_names[0]






