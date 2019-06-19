import cv2
import matplotlib.pyplot as plt
import numpy as np

img = cv2.imread('./images/crossword.jpg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
img_ori = img.copy()
# kernel = np.random.randint(0, 2, (5, 5), dtype=np.uint8)/10
# img = cv2.filter2D(img, -1, kernel)
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

img_bitwise = cv2.bitwise_not(img)

ret, th1 = cv2.threshold(img, 40, 255, cv2.THRESH_BINARY_INV)
th2 = cv2.adaptiveThreshold(
    img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY_INV, 7, 10)

final_img = cv2.addWeighted(th1, 0.4, th2, 0.6, 0)


wb = np.full(img_ori.shape, 255, np.uint8)

wb[:, :, 0] = 0
wb[:, :, 2] = 0

img_mask = cv2.bitwise_or(wb, wb, mask=final_img)

final = cv2.bitwise_or(img_ori, img_mask)

concat = np.concatenate((img_ori, final), 1)

plt.imshow(concat, 'gray')
plt.show()
