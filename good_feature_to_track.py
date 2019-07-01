import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('./images/real_chess.jpg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
corners = cv2.goodFeaturesToTrack(img, 100, 0.01, 10)
corners = np.int0(corners)

for i in corners:
    x, y = i.ravel()
    cv2.circle(img, (x, y), 3, (0, 0, 255), -1)
plt.imshow(img)
plt.show()