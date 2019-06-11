import cv2
import matplotlib.pyplot as plt


img1 = cv2.imread('puppy.jpg')
img2 = cv2.imread('haydane.jpg')

img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)
img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)


# 3 blended image with same size
# img1 = cv2.resize(src=img1, dsize=(1200, 1200))
# img2 = cv2.resize(src=img2, dsize=(1200, 1200))
# blended_img = cv2.addWeighted(
# src1=img1, alpha=0.5, src2=img2, beta=0.5, gamma=0)


# blended image with different size
large_img = img1
small_img = img2


x_offset = 0
y_offset = 0

x_end = x_offset + small_img.shape[1]
y_end = x_offset + small_img.shape[0]

large_img[y_offset:y_end, x_offset:x_end] = small_img

# cv2.imwrite('new_img.jpg', large_img)
plt.imshow(large_img)
plt.show()
