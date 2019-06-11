import cv2
import numpy as np
import matplotlib.pyplot as plt


def displyImg(img):
    fig = plt.figure(figsize=(50, 50))
    fig = fig.add_subplot(111)
    fig.imshow(img, cmap='gray')
    plt.show()


img = cv2.imread('./sudoku.jpg', 0)

# sobel discovers x or y line in the picture of gradient
sobelx = cv2.Sobel(src=img, ddepth=cv2.CV_64F, dx=1, dy=0, ksize=5)
sobely = cv2.Sobel(src=img, ddepth=cv2.CV_64F, dx=0, dy=1, ksize=5)

# laplacian great edge detection, more clear
laplacian = cv2.Laplacian(img, cv2.CV_64F)


# blending images

blended = cv2.addWeighted(src1=sobelx, alpha=0.5,
                          src2=sobely, beta=0.5, gamma=0.5)


concat = np.concatenate((sobelx, sobely, blended, laplacian), 1)


# threshold, convert img to black and white
ret, th1 = cv2.threshold(img, 100, 255, cv2.THRESH_BINARY)

# gradient
kernel = np.ones((5, 5), np.uint8)
gradient = cv2.morphologyEx(blended, cv2.MORPH_GRADIENT, kernel)

displyImg(concat)
