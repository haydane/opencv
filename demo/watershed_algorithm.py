import cv2
import matplotlib.pyplot as plt
import numpy as np


def display(img, cmap='gray'):
    fig = plt.figure(figsize=(12, 10))
    fig = fig.add_subplot(111)
    fig.imshow(img, cmap='gray')
    plt.show()

# median blur
# grayscale
# binary threshold
# find contour


coin = cv2.imread('../images/coin.jpg')
coin_copy = coin.copy()
blur_coin = cv2.medianBlur(coin, ksize=35)
gray_coin = cv2.cvtColor(blur_coin, cv2.COLOR_BGR2GRAY)

# ret, thresh = cv2.threshold(gray_coin, 160, 255, cv2.THRESH_BINARY_INV)

# image, contours, hierarchy = cv2.findContours(
#     thresh.copy(), cv2.RETR_CCOMP, cv2.CHAIN_APPROX_SIMPLE)

# for i in range(len(contours)):
#     if hierarchy[0][i][3] == -1:
#         cv2.drawContours(coin, contours, i, (255, 0, 0), 10)
# display(coin)


# Second Method
ret, thresh = cv2.threshold(
    gray_coin, 0, 255, cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)


# noise removal (optional)
kernel = np.ones((3, 3), np.uint8)

opening = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel, iterations=2)


sure_bg = cv2.dilate(opening, kernel, iterations=3)

dist_transform = cv2.distanceTransform(opening, cv2.DIST_L2, 5)

ret, sure_fg = cv2.threshold(dist_transform, 0.7*dist_transform.max(), 255, 0)


sure_fg = np.uint8(sure_fg)

unknown = cv2.subtract(sure_bg, sure_fg)
ret, markers = cv2.connectedComponents(sure_fg)
markers = markers + 1

markers[unknown == 255] = 0

# apple watershed

markers = cv2.watershed(coin, markers)


image, contours, hierarchy = cv2.findContours(
    markers.copy(), cv2.RETR_CCOMP, cv2.CHAIN_APPROX_SIMPLE)

for i in range(len(contours)):
    if hierarchy[0][i][3] == -1:
        cv2.drawContours(coin, contours, i, (255, 0, 0), 10)


plt.subplot(431)
plt.imshow(coin_copy, cmap='gray')
plt.title('coin_copy')

plt.subplot(432)
plt.imshow(blur_coin, cmap='gray')
plt.title('blur_coin')

plt.subplot(433)
plt.imshow(gray_coin, cmap='gray')
plt.title('gray_coin')

plt.subplot(434)
plt.imshow(thresh, cmap='gray')
plt.title('thresh')


plt.subplot(435)
plt.imshow(opening, cmap='gray')
plt.title('reduce noise')

plt.subplot(436)
plt.imshow(sure_bg, cmap='gray')
plt.title('increase white region')


plt.subplot(437)
plt.imshow(dist_transform, cmap='gray')
plt.title('representation of a binary image')


plt.subplot(438)
plt.imshow(sure_fg, cmap='gray')
plt.title('foreground')

plt.subplot(439)
plt.imshow(unknown, cmap='gray')
plt.title('subtract')


plt.subplot(4, 3, 10)
plt.imshow(markers, cmap='gray')
plt.title('apply watershed')

plt.subplot(4, 3, 11)
plt.imshow(coin, cmap='gray')
plt.title('Final')


plt.suptitle('Watershed Algorithim')
plt.show()
