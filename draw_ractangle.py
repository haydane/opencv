import cv2
import matplotlib.pyplot as plt
import numpy as np

# Variable
ix, iy = -1, -1
drawing = False

# Event


def draw_rec(event, x, y, flags, param):
    global ix, iy, drawing

    if event == cv2.EVENT_LBUTTONDOWN:
        ix, iy = x, y
        drawing = True
    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing == True:
            cv2.rectangle(blank_img, pt1=(ix, iy), pt2=(x, y),
                          color=(255, 255, 255), thickness=-1)
    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        cv2.rectangle(blank_img, pt1=(ix, iy), pt2=(x, y),
                      color=(255, 255, 255), thickness=-1)


cv2.namedWindow(winname='Rec')
cv2.setMouseCallback('Rec', draw_rec)

# Windows
blank_img = np.zeros((512, 512, 3), dtype=np.uint8)

while True:
    cv2.imshow('Rec', blank_img)
    if cv2.waitKey(200) & 0xFF == 27:
        break

cv2.destroyAllWindows()
