import cv2
import numpy as np
import matplotlib.pyplot as plt
img = cv2.imread('./images/Dog-Backpack-Carriers.jpg')
img = cv2.cvtColor(src=img, code=cv2.COLOR_BGR2RGB)
face = img[380:720, 200:640]


methods = ['cv2.TM_CCOEFF', 'cv2.TM_CCOEFF_NORMED', 'cv2.TM_CCORR',
           'cv2.TM_CCORR_NORMED', 'cv2.TM_SQDIFF', 'cv2.TM_SQDIFF', 'cv2.TM_SQDIFF_NORMED']

for m in methods:
    # create a copy of image
    img_copy = img.copy()
    method = eval(m)

    # template matching
    res = cv2.matchTemplate(img_copy, face, method)

    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

    if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
        top_left = min_loc  # (x,y)
    else:
        top_left = max_loc

    height, width, channels = face.shape

    bottom_right = (top_left[0] + width, top_left[1] + height)

    cv2.rectangle(img_copy, top_left, bottom_right, (255, 0, 0), 10)

    # plot and show the image
    fig = plt.figure(figsize=(12, 10))

    plt.subplots(121)
    plt.imshow(res)
    plt.title('HEATMAP OF TEMPLATE MATCHING')

    plt.subplots(122)
    plt.imshow(img_copy)
    plt.title('DETECTION OF TEMPLATE')
    plt.suptitle(m)
    plt.show()

print('\n')
print('\n')
