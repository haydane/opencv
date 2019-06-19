import cv2
import numpy as np
import matplotlib.pyplot as plt


nadia = cv2.imread('./images/Nadia_Murad.jpg', 0)
denis = cv2.imread('./images/Denis_Mukwege.jpg', 0)
solvay = cv2.imread('./images/solvay_conference.jpg', 0)

face_cascade = cv2.CascadeClassifier(
    '../Document/Computer-Vision-with-Python/DATA/haarcascades/haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier(
    '../Document/Computer-Vision-with-Python/DATA/haarcascades/haarcascade_eye.xml')


def detect_face(img):
    face_img = img.copy()
    face_rects = face_cascade.detectMultiScale(face_img)
    for (x, y, w, h) in face_rects:
        cv2.rectangle(face_img, (x, y), (x+w, y+h), (0, 255, 0), 3)
    return face_img


def adj_detect_face(img):
    face_img = img.copy()
    face_rects = face_cascade.detectMultiScale(
        face_img, scaleFactor=1.3, minNeighbors=5)
    for (x, y, w, h) in face_rects:
        cv2.rectangle(
            face_img, (x, y), (x+w, y+h), (0, 255, 0), 3)
    return face_img


def detect_eyes(img):
    face_img = img.copy()
    eye_rects = eye_cascade.detectMultiScale(
        face_img, scaleFactor=1.3, minNeighbors=5)
    for (x, y, w, h) in eye_rects:
        cv2.rectangle(face_img, (x, y), (x+w, y+h), (0, 255, 0), 3)
    return face_img


# res = detect_eyes(nadia)

# print(nadia.shape)
# plt.imshow(res, cmap='gray')
# plt.show()

cap = cv2.VideoCapture(0)
# cap.set(cv2.CAP_PROP_FRAME_WIDTH, 300)
# cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 300)
while True:
    ret, frame = cap.read(0)
    frame = detect_face(frame)
    cv2.imshow('Video Capture', frame)

    k = cv2.waitKey(1)
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()
