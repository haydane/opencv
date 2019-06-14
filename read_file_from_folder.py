import cv2
import glob
import matplotlib.pyplot as plt
import numpy as np


def display(img, cmap='gray'):
    fig = plt.figure(figsize=(12, 10))
    fig = fig.add_subplot(111)
    fig.imshow(img, cmap='gray')
    plt.show()


path = "./images/*.png"


def feature_matching(img, path):
    sift = cv2.xfeatures2d.SIFT_create()
    kp1, des1 = sift.detectAndCompute(img, None)
    for file in glob.glob(path):
        file_name = cv2.imread(file, 0)

        kp2, des2 = sift.detectAndCompute(file_name, None)
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
                good.append(match1)
        if len(good) > 80:
            print(file)


reeses = cv2.imread('./images/reeses-puffs.png', 0)
feature_matching(reeses, path)
