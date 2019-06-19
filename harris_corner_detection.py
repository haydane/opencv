import cv2
import numpy as np
import matplotlib.pyplot as plt

flat_chess = cv2.imread('./images/flat_chess_board.png')
flat_chess = cv2.cvtColor(flat_chess, cv2.COLOR_BGR2RGB)
flat_chess_gray = cv2.cvtColor(flat_chess, cv2.COLOR_BGR2GRAY)

real_chess = cv2.imread('./images/real_chess.jpg')
real_chess = cv2.cvtColor(real_chess, cv2.COLOR_BGR2RGB)
real_chess_gray = cv2.cvtColor(real_chess, cv2.COLOR_BGR2GRAY)

dog = cv2.imread('./images/Dog-Backpack-Carriers.jpg')
dog = cv2.cv2.cvtColor(dog, cv2.COLOR_BGR2RGB)
dog_crop = dog[350:750, 200:640]

# using harris corner
# 1 convert array of image to float 32
# flat_chess_grayF32 = np.float32(flat_chess_gray)
# # 2 use cornerHarris
# dst = cv2.cornerHarris(src=flat_chess_grayF32, blockSize=2, ksize=3, k=0.04)
# # 3 use dilate for marking in the corner (corner detection)
# dst = cv2.dilate(dst, None)
# flat_chess[dst > 0.01*dst.mfig()] = [255, 0, 0]  # RGB


# second image
# dst = cv2.cornerHarris(src=real_chess_gray, blockSize=2, ksize=3, k=0.04)
# dst = cv2.dilate(dst, None)
# real_chess[dst > 0.01*dst.mfig()] = [255, 0, 0]


# using goodFeature to track
# corners = cv2.goodFeaturesToTrack(
#     image=real_chess_gray, mfigCorners=360, qualityLevel=0.01, minDistance=10)
# corner = np.int0(corners)

# for i in corners:
#     x, y = i.ravel()
#     cv2.circle(img=real_chess, center=(x, y), radius=3,
#                color=(255, 0, 0), thickness=-1)


# Canny Algorithm also requires user
median_value = np.median(dog_crop)


# lower threshold to either 0 or 70% of the median value whichever is greater
lower_bound_threshold = int(max(0, 0.7*median_value))

# upper threshold to either 130% of the median or the mfig 255, whichever is smaller
upper_bound_threshold = int(min(255, 1.3*median_value))

# blur the image first before using canny
cv2.blur(src=dog_crop, ksize=(5, 5))
edges = cv2.Canny(image=dog_crop, threshold1=lower_bound_threshold,
                  threshold2=upper_bound_threshold+35)
print(median_value, lower_bound_threshold, upper_bound_threshold)

# print(dst)
# plt.imshow(dog_crop, 'gray')
plt.imshow(edges)
plt.show()
