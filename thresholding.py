import cv2
import matplotlib.pyplot as plt

img = cv2.imread('./images/rainbow.jpg', 0)
# thresholding
ret, thresh1 = cv2.threshold(img, 90, 255, cv2.THRESH_BINARY)
# print(thres)

plt.imshow(thresh1, cmap='gray')
plt.show()
1
