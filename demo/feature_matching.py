import cv2
import matplotlib.pyplot as plt
import numpy as np


def display(img, cmap='gray'):
    fig = plt.figure(figsize=(12, 10))
    fig = fig.add_subplot(111)
    fig.imshow(img, cmap='gray')
    plt.show()


reeses = cv2.imread('../images/reeses-puffs.png', 0)
cereals = cv2.imread('../images/many_cereal.jpg', 0)


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
#     reeses, kp1, cereals, kp2, matches[:100], None, flags=2)

# display(reeses_matches)


# # second method

# sift = cv2.xfeatures2d.SIFT_create()
# kp1, des1 = sift.detectAndCompute(reeses, None)
# kp2, des2 = sift.detectAndCompute(cereals, None)

# bf = cv2.BFMatcher()

# matches = bf.knnMatch(des1, des2, k=2)

# good = []

# # less distance == better match

# # ratio match1 < 75% match 2


# for match1, match2 in matches:
#     print("match1", match1.distance)
#     print("match2", match2.distance)
#     if match1.distance < 0.75 * match2.distance:
#         good.append([match1])

# sift_matches = cv2.drawMatchesKnn(
#     reeses, kp1, cereals, kp2, good, None, flags=2)

# display(sift_matches)


# third

sift = cv2.xfeatures2d.SIFT_create()
kp1, des1 = sift.detectAndCompute(reeses, None)
kp2, des2 = sift.detectAndCompute(cereals, None)
# flann
FLANN_INDEX_KDTREE = 0
index_params = dict(algorithm=FLANN_INDEX_KDTREE, trees=5)
search_params = dict(checks=50)

flann = cv2.FlannBasedMatcher(index_params, search_params)

matches = flann.knnMatch(des1, des2, k=2)

matchesMask = [[0, 0] for i in range(len(matches))]


good = []

for i, (match1, match2) in enumerate(matches):
    if match1.distance < 0.7 * match2.distance:
        matchesMask[i] = [1, 0]

draw_params = dict(matchColor=(0, 0, 255), singlePointColor=(
    255, 0, 0), matchesMask=matchesMask, flags=2)

flann_matches = cv2.drawMatchesKnn(
    reeses, kp1, cereals, kp2, matches, None, **draw_params)

display(flann_matches)
