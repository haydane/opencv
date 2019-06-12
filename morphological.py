import cv2
import matplotlib.pyplot as plt
import numpy as np

# Create blank image with text
blank_img = np.zeros((600, 600))
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(blank_img, text='ABCDE', org=(50, 300), fontFace=font,
            fontScale=5, color=(255, 255, 255), thickness=17)

# customer kernel
kernel = np.ones((5, 5), dtype=np.uint8)

# erosion
erode = cv2.erode(blank_img, kernel, iterations=1)

# dilation
# Create white noise
white_noise = np.random.randint(0, 2, (600, 600))
white_noise = white_noise * 255

# Introducing noise into blank_img
noise_img = white_noise + blank_img

# Using opening to get rid of the background noise
# Opening = erosion followed by dilation
opening = cv2.morphologyEx(noise_img, cv2.MORPH_OPEN, kernel)

# Create black noise
black_noise = np.random.randint(0, 2, (600, 600))
black_noise = black_noise * -255
black_noise_img = blank_img + black_noise

# Bring back the -255 to 0
black_noise_img[black_noise_img == -255] = 0

# Using closing to get rid of the foreground noise
closing = cv2.morphologyEx(black_noise_img, cv2.MORPH_CLOSE, kernel)


# Morphological Gradient (Edge Detection)
# It takes the different of the erosion and dilation
# erosion will get rid between background and forground edge
# Dilation will end up adding more bubbly to the image
gradient = cv2.morphologyEx(blank_img, cv2.MORPH_GRADIENT, kernel)

compare = np.concatenate((blank_img, erode, opening, closing, gradient), 1)
plt.imshow(noise_img, cmap='gray')
plt.show()
# print(white_noise)
