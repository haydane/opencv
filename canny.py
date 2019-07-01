import cv2
import matplotlib.pyplot as plt

img = cv2.imread('./images/black-face.png', 0)

edges = cv2.Canny(img, 100, 200)

plt.subplot(121), plt.imshow(img, cmap='gray')

plt.title('Before')

plt.subplot(122), plt.imshow(edges, cmap='gray')
plt.title('after')

plt.suptitle('testing')
plt.show()
