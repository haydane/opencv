import cv2
import matplotlib.pyplot as plt
import numpy as np

img = cv2.imread('./images/plane.jpg')
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

ret, thresh = cv2.threshold(img_gray, 127, 255, 0)

img2, contours, hierachy = cv2.findContours(thresh, cv2.RETR_TREE,
                                            cv2.CHAIN_APPROX_SIMPLE)

# change color
# img = cv2.bitwise_not(img, img)

# img[:, :, 0] = 0
# img[:, :, 2] = 0

# all outline value = -1
# cv2.drawContours(img, contours, -1, (255, 0, 0), 1)

# if value of hierachy == -1, outline
# if value of hierachy !=-1 inline
for i in range(len(contours)):
    if hierachy[0][i][3] != -1:
        cv2.drawContours(img, contours, i, (255, 0, 0), 2)

plt.imshow(img)
plt.show()