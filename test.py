import cv2
import matplotlib.pyplot as plt
import numpy as np

# read image
img1 = cv2.imread('./Dog-Backpack-Carriers.jpg')
img2 = cv2.imread('./do-not-copy.png')

# convert image
img1 = cv2.cvtColor(src=img1, code=cv2.COLOR_BGR2RGB)
img2 = cv2.cvtColor(src=img2, code=cv2.COLOR_BGR2RGB)

# resize image
img2 = cv2.resize(src=img2, dsize=(300, 300))

# offset image
x_offset = img1.shape[1] - img2.shape[1]
y_offset = img1.shape[0] - img2.shape[0]

img_offset = img1[y_offset:img1.shape[0], x_offset:img1.shape[1]]

# gray image
gray_img = cv2.cvtColor(src=img2, code=cv2.COLOR_BGR2GRAY)

# invert_img
bitwise_img = cv2.bitwise_not(src=gray_img)

# white background
white_background = np.full(img2.shape, 255, np.uint8)


# Apply 3 channel to mask
bk = cv2.bitwise_or(white_background, white_background, mask=bitwise_img)
fg = cv2.bitwise_or(img2, img2, mask=bitwise_img)

final = cv2.bitwise_or(img_offset, fg)
large_img = img1
small_img = final

large_img[y_offset:img1.shape[0], x_offset:img1.shape[1]] = small_img

plt.imshow(large_img)
plt.show()
