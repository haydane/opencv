import cv2
import matplotlib.pyplot as plt
import numpy as np

img1 = cv2.imread('./images/puppy.jpg')
img2 = cv2.imread('./images/do-not-copy.png')

img1 = cv2.cvtColor(src=img1, code=cv2.COLOR_BGR2RGB)
img2 = cv2.cvtColor(src=img2, code=cv2.COLOR_BGR2RGB)

img2 = cv2.resize(src=img2, dsize=(300, 300))

# Find offset
opencv_x_offset = img1.shape[1] - img2.shape[1]
opencv_y_offset = img1.shape[0] - img2.shape[0]

# Get offset Image
offset_img = img1[opencv_y_offset:img1.shape[0], opencv_x_offset:img1.shape[1]]

img2_gray = cv2.cvtColor(src=img2, code=cv2.COLOR_RGB2GRAY)

# Inverse image
mask_inv = cv2.bitwise_not(src=img2_gray)

# Get 3 channel
white_background = np.full(img2.shape, 255, dtype=np.uint8)

# Apply 3 channel to mask
bk = cv2.bitwise_or(white_background, white_background, mask=mask_inv)
fg = cv2.bitwise_or(img2, img2, mask=mask_inv)

final = cv2.bitwise_or(offset_img, fg)

large_img = img1
small_img = final

large_img[opencv_y_offset:img1.shape[0],
          opencv_x_offset:img1.shape[1]] = small_img


plt.imshow(offset_img)
plt.show()
