# display the frequency value for colors
import cv2
import matplotlib.pyplot as plt
import numpy as np
dog = cv2.imread('./Dog-Backpack-Carriers.jpg')
show_dog = cv2.cvtColor(dog, cv2.COLOR_BGR2RGB)
dane = cv2.imread('./haydane.jpg')
show_dane = cv2.cvtColor(dane, cv2.COLOR_BGR2RGB)
rainbow = cv2.imread('./rainbow.jpeg')
show_rainbow = cv2.cvtColor(rainbow, cv2.COLOR_BGR2RGB)
gorilla = cv2.imread('./gorilla.jpg')
gray_gorilla = cv2.imread('./gorilla.jpg', 0)
color_gorilla = cv2.cvtColor(gorilla, cv2.COLOR_BGR2RGB)

# use calcHist to get histogram value
# pass the original image
histr1 = cv2.calcHist(images=[dog], channels=[0],
                      mask=None, histSize=[256], ranges=[0, 256])

# img = dane

# color = ('r', 'g', 'b')
# for i, col in enumerate(color):
#     histr2 = cv2.calcHist([img], [i], None, [256], [0, 256])
#     plt.plot(histr2, color=col)
# in case we get very large hisgram that extends beyond 256
# plt.xlim([0, 256])
# plt.ylim([0, 100])


# histogram eqaulizaion

# 1. create a mask image same size to show_dane pic
mask = np.zeros(show_rainbow.shape[:2], dtype=np.uint8)

# 2. draw white rectangle to the mask
# mask[100:140, 50:300] = 255

# 3. apply image to the mask for histogram calculation
# masked_image = cv2.bitwise_and(show_rainbow, show_rainbow, mask=mask)

# 4. histogram with and without mask
# show_mask_value_red = cv2.calcHist(images=[rainbow], channels=[
#                                    2], mask=mask, histSize=[256], ranges=[0, 256])
# show_value_red = cv2.calcHist(images=[rainbow], channels=[
#                               2], mask=None, histSize=[256], ranges=[0, 256])


def displyImg(img, cmap=None):
    fig = plt.figure(figsize=(50, 50))
    fig = fig.add_subplot(111)
    fig.imshow(img, cmap='gray')
    plt.show()


# Histogram Equalization
eq_gorilla = cv2.equalizeHist(gray_gorilla)  # much higher contrast
hist_value = cv2.calcHist(images=[eq_gorilla], channels=[
                          0], mask=None, histSize=[256], ranges=[0, 256])


# 1. hsv to color grilla
# 0 channel is hue, 1 is situration, 2 is value channel
hsv_gorilla = cv2.cvtColor(color_gorilla, cv2.COLOR_BGR2HSV)

# 2. replace hue value from equalize value to hsv
hsv_gorilla[:, :, 2] = cv2.equalizeHist(hsv_gorilla[:, :, 2])

# 3. convert hsv to rgb
eq_color_gorilla = cv2.cvtColor(hsv_gorilla, cv2.COLOR_HSV2RGB)

displyImg(eq_color_gorilla)

# plt.title('HISTOGRAM FOR DANE')
# concat = np.concatenate((show_mask_value_red, show_value_red), 1)
