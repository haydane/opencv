import cv2
import matplotlib.pyplot as plt

img = cv2.imread('./images/dot1.jpg')
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

ret, thresh = cv2.threshold(img_gray, 127, 255, cv2.THRESH_BINARY)
im2, contours, hierachy = cv2.findContours(thresh, cv2.RETR_TREE,
                                           cv2.CHAIN_APPROX_NONE)

# print("contours", contours)
# print("hierachy", hierachy)

hull = [cv2.convexHull(c) for c in contours]

final = cv2.drawContours(img, hull, -1, (0, 0, 255), 3)
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

plt.imshow(img, cmap='gray')
plt.show()