import numpy as np
import cv2


def draw_circle(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img, (x, y), 50, (0, 255, 0), -1)
    elif event == cv2.EVENT_RBUTTONDOWN:
        cv2.circle(img, (x, y), 50, (155, 0, 0), -1)


cv2.namedWindow(winname='my_drawing')
cv2.setMouseCallback('my_drawing', draw_circle)


img = np.zeros(shape=(512, 512, 3))

while True:
    cv2.imshow('my_drawing', img)
    if cv2.waitKey(20) & 0xFF == 27:
        break
cv2.destroyAllWindows()
