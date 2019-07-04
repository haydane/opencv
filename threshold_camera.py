import cv2
import matplotlib.pyplot as plt

cap = cv2.VideoCapture(0)

face_cascade = cv2.CascadeClassifier(
    '../Document/Computer-Vision-with-Python/DATA/haarcascades/haarcascade_frontalface_default.xml'
)


def convex_hull(img):
    img_gray = img.copy()
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    ret, thresh = cv2.threshold(img_gray, 127, 255,
                                cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    im2, contours, hierachy = cv2.findContours(thresh, cv2.RETR_EXTERNAL,
                                               cv2.CHAIN_APPROX_SIMPLE)

    hull = [cv2.convexHull(c) for c in contours]

    cv2.drawContours(img, hull, -1, 255, 3)
    # for i in range(len(contours)):
    #     if hierachy[0][i][3] == -1:
    #         cv2.drawContours(img, hull, i, (0, 0, 255), 2)
    # return img


def face_detection(face):
    face_img = face.copy()
    face_rect = face_cascade.detectMultiScale(face_img)
    for x, y, w, h in face_rect:
        cv2.rectangle(face, (x, y), (x + h, y + h), (0, 0, 255), 3)
    return face


def cvt2Threshold(img):
    img_copy = img.copy()
    img_gray = cv2.cvtColor(img_copy, cv2.COLOR_BGR2GRAY)
    ret, thresh = cv2.threshold(img_gray, 127, 255,
                                cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    img2, contours, hierachy = cv2.findContours(thresh, cv2.RETR_TREE,
                                                cv2.CHAIN_APPROX_SIMPLE)

    for i in range(len(contours)):
        if hierachy[0][i][3] == -1:
            cv2.drawContours(img, contours, i, (0, 0, 255), 1)

    return img


while True:
    ret, frame = cap.read(0)

    k = cv2.waitKey(1)
    if k & 0xff == 27:
        break

    convex_hull(frame)
    # face_detection(frame)
    # frame = cvt2Threshold(frame)
    cv2.imshow('frame', frame)
cap.release()
cv2.destroyAllWindows()

cv2.polylines()
