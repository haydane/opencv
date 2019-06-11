import cv2
import matplotlib.pyplot as plt
import numpy as np


def display(img, cmap='gray'):
    fig = plt.figure(figsize=(12, 10))
    fig = fig.add_subplot(111)
    fig.imshow(img, cmap='gray')
    plt.show()


reeses = cv2.imread('./images/reeses-puffs.png', 0)
cereals = cv2.imread('./images/many cereal.jpg', 0)


# # 1. get key point sudo apt-get updateand descripter
# # create a detecter object
# # kp is key point
# # des = destination
# orb = cv2.ORB_create()
# kp1, des1 = orb.detectAndCompute(reeses, None)
# kp2, des2 = orb.detectAndCompute(cereals, None)

# # 2. match and sorted
# # bf = brute force
# bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
# matches = bf.match(des1, des2)

# matches = sorted(matches, key=lambda x: x.distance)

# # 25 is number of matched lines
# reeses_matches = cv2.drawMatches(
#     reeses, kp1, cereals, kp2, matches[:25], None, flags=2)

# display(reeses_matches)


# second method
sift = cv2.xfeatures2d_SIFT_create()
kp1, des1 = sift.detectAndCompute(reeses, None)
kp2, des2 = sift.detectAndCompute(cereals, None)

bf = cv2.BFMatcher()

matches = bf.knnMatcher()

# good = []
# for match1 in matches:
#     print(match1)

# print(len(des1))


# # 25 is number of matched lines
# reeses_matches = cv2.drawMatches(
#     reeses, kp1, cereals, kp2, matches[:25], None, flags=2)

# display(reeses_matches)
