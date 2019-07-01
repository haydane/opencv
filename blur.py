import cv2
import matplotlib.pyplot as plt
import numpy as np


def displayImg(img):
    plt.imshow(img)
    plt.show()


def convertImg(img):
    img = cv2.cvtColor(img, code=cv2.COLOR_BGR2RGB)
    return img


img = cv2.imread('./images/noise.jpg')
img = convertImg(img)
# img = cv2.resize(img, (100, 100))
# cv2.putText(img=img, text='BAB', org=(20, 500), fontFace=cv2.FONT_HERSHEY_COMPLEX,
#             fontScale=8, color=(0, 255, 0), thickness=10)
# img_blur = cv2.medianBlur(img, ksize=15)

# img_noise = np.random.randint(0, 2, (600, 600, 3), np.uint8)


# compare = np.concatenate((img, img_blur), 1)


# img2 = cv2.imread('./noise.jpg')
# img2 = convertImg(img2)
# reduce_noise = cv2.GaussianBlur(img2, (5, 5), 5)


# kernel = np.ones((5, 5), np.uint8)/25
# kernel = np.random.randint(0, 2, (5, 5), dtype=np.uint8)/10
# print(kernel)
# result = cv2.filter2D(img, -1, kernel)

# concat = np.concatenate((img, result), 1)
# displayImg(concat)


# gaussianBlur
displayImg(cv2.GaussianBlur(img, (11, 11), 100))
