import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('../images/car_plate.jpg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)


def display(img):
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111)
    new_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    ax.imshow(new_img)
    plt.show()


plate_cascade = cv2.CascadeClassifier(
    '../../Document/Computer-Vision-with-Python/DATA/haarcascades/haarcascade_russian_plate_number.xml')


def detect_plate(img):
    plate_img = img.copy()
    plate_rec = plate_cascade.detectMultiScale(
        plate_img, scaleFactor=1.3, minNeighbors=3)
    for (x, y, w, h) in plate_rec:
        cv2.rectangle(plate_img, (x, y), (x+w, y+h), (255, 0, 0), 2)
    return plate_img


def detect_and_blur_plate(img):
    plate_img = img.copy()
    roi = img.copy()

    plate_rects = plate_cascade.detectMultiScale(
        plate_img, scaleFactor=1.3, minNeighbors=3)

    for (x, y, w, h) in plate_rects:
        roi = roi[y:y+h, x:x+w]
    blur_roi = cv2.medianBlur(roi, 101)
    plate_img[y:y+h, x:x+w] = blur_roi

    return plate_img


result_draw_rec = detect_plate(img)
result_blur = detect_and_blur_plate(img)


plt.subplot(121)
plt.imshow(result_draw_rec)
plt.title('Detect and Draw')

plt.subplot(122)
plt.imshow(result_blur)
plt.title('Detect and Blur')

plt.suptitle('Plate Detection')
plt.show()


# display(result_draw_rec)
# display(result_blur)
