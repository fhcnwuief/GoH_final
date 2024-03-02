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
from sklearn.metrics import confusion_matrix, roc_curve, auc, f1_score, precision_recall_curve, roc_auc_score

class FaceLoader:
    def __init__(self, directory):
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
                path = os.path.join(dir, im_name)
                single_face = self.extract_face(path)
                FACES.append(single_face)
            except Exception as e:
                pass
        return FACES

    def load_classes(self):
        for sub_dir in os.listdir(self.directory):
            path = os.path.join(self.directory, sub_dir)
            FACES = self.load_faces(path)
            labels = [sub_dir for _ in range(len(FACES))]
            self.X.extend(FACES)
            self.Y.extend(labels)
        return np.asarray(self.X), np.asarray(self.Y)

# Load faces and embeddings
faceloader = FaceLoader("camera/dataset")
X, Y = faceloader.load_classes()

# Use Facenet for embedding extraction
embedder = FaceNet()
X_embedded = [embedder.embeddings(img.astype("float32").reshape((1, 160, 160, 3)))[0] for img in X]
X_embedded = np.asarray(X_embedded)

# Declare encoder as a global variable
encoder = LabelEncoder()
encoder.fit(Y)
Y_encoded = encoder.transform(Y)

# Split the data into training and testing sets
X_train, X_test, Y_train, Y_test = train_test_split(X_embedded, Y_encoded, shuffle=True, random_state=17)

# Train the SVM model
model = SVC(kernel="linear", probability=True)
model.fit(X_train, Y_train)

# Model predictions
y_pred = model.predict(X_test)
y_pred_labels = encoder.inverse_transform(y_pred)

# Confusion Matrix
cm = confusion_matrix(Y_test, y_pred_labels)
print("Confusion Matrix:")
print(cm)

# ROC Curve and AUC-ROC
fpr, tpr, thresholds = roc_curve(Y_test, y_pred_labels)
auc_roc = auc(fpr, tpr)

plt.figure(figsize=(8, 8))
plt.plot(fpr, tpr, color='darkorange', lw=2, label=f'AUC = {auc_roc:.2f}')
plt.plot([0, 1], [0, 1], color='navy', lw=2, linestyle='--')
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('Receiver Operating Characteristic (ROC) Curve')
plt.legend(loc="lower right")
plt.show()

print(f"AUC-ROC: {auc_roc:.2f}")

# F1 Score
f1 = f1_score(Y_test, y_pred_labels, average='weighted')
print(f"F1 Score: {f1:.2f}")