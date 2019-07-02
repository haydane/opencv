import cv2
import matplotlib.pyplot as plt
import numpy as np

# contours are a useful tool for shape analysis and object detection and recognition

# pass 0 to read as a gray scale
smiley = cv2.imread('./images/internal_external.png', 0)
# plt.imshow(smiley, cmap='gray')
# internal and external contour
image, contours, hirerachy = cv2.findContours(smiley, cv2.RETR_CCOMP,
                                              cv2.CHAIN_APPROX_SIMPLE)

# print(type(contours), len(contours), type(hirerachy))
# print(list(range(len(contours))))
# print(hirerachy)

print("=====================================+>", hirerachy)

print("-----------------------> ", hirerachy[0][0][3], hirerachy[0][1][3],
      hirerachy[0][2][3])
# copy image shape
external_contours = np.zeros(smiley.shape)
internal_contours = np.zeros(smiley.shape)

for i in range(len(contours)):
    # 0 is for each row and 3 is last column
    # external_contour

    if hirerachy[0][i][3] == -1:
        cv2.drawContours(external_contours, contours, i, 255, -1)

for i in range(len(contours)):
    # 0 is for each row and 3 is last column
    # external_contour

    if hirerachy[0][i][3] != -1:
        cv2.drawContours(internal_contours, contours, i, 255, -1)

print
plt.subplot(121)
plt.imshow(external_contours, cmap='gray')
plt.title('External Contour')

plt.subplot(122)
plt.imshow(internal_contours, cmap='gray')
plt.title('Internal Contour')

plt.suptitle('Contour Detection')
plt.show()

plt.show()
