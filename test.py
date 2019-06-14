import cv2
import matplotlib.pyplot as plt
import numpy as np

img = cv2.imread('./images/internal_external.png')
img_copy = img.copy().astype(np.int16)

black_bg = np.zeros((100, 100, 3), np.uint8)

cv2.putText(black_bg, "i", (10, 80),
            cv2.FONT_HERSHEY_SIMPLEX, 3, (255, 0, 0), 3)
kernel = np.ones((3, 3), np.uint8)
black_bg = cv2.erode(black_bg, kernel, 3)

dilation = cv2.dilate(black_bg, kernel, 1)

# img_copy = img.copy()
print(img.shape)


# 131 : 1 row, 3 column picture 1th
plt.subplot(131)
plt.title('image')
plt.imshow(img)

plt.subplot(132)
plt.title('image copy')
plt.imshow(img_copy+3)

plt.subplot(133)
plt.title('black image')
plt.imshow(dilation)

plt.suptitle('Comparation')

plt.show()
# while True:
#     cv2.imshow('frame', img1)
#     if cv2.waitKey(1) == 27:
#         break
# cv2.destroyAllWindows()
