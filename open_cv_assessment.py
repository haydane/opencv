import cv2
import numpy as np
import matplotlib.pyplot as plt

# read img
img = cv2.imread('./images/Dog-Backpack-Carriers.jpg')

# fix img
img_convert = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)


# flip img
img_flip = np.flip(img_convert, axis=0)

# draw rectange on dog's face
# draw_rec = cv2.rectangle(
#     img_convert, pt1=(200, 400), pt2=(627, 737), color=(0, 255, 0), thickness=10)


# draw triangle

# pt1 = (448, 360)
# pt2 = (215, 706)
# pt3 = (644, 706)

# triangle_corner = np.array([pt1, pt2, pt3])
# cv2.drawContours(img_convert, [triangle_corner], 0, (0, 0, 255), 15)
# cv2.circle(img, pt1, 2, (0, 0, 255), -1)
# cv2.circle(img, pt2, 2, (0, 0, 255), -1)
# cv2.circle(img, pt3, 2, (0, 0, 255), -1)


# one more thing
np_arr = [[448, 360], [215, 706], [644, 706]]
np_victor = np.asarray(np_arr)

reshape_arr = np_victor.reshape(1, -1, 2)
# cv2.polylines(img=img_convert, pts=reshape_arr, isClosed=True,
#               color=(0, 0, 255), thickness=10)

cv2.fillPoly(img=img_convert, pts=reshape_arr, color=(0, 0, 255))
plt.imshow(img_convert)
plt.show()

# fill triangle

# pt1 = (448, 360)
# pt2 = (215, 706)
# pt3 = (644, 706)

# triangle_corner = np.array([pt1, pt2, pt3])
# cv2.drawContours(img_convert, [triangle_corner], 0, (0, 0, 255), -1)
# cv2.circle(img, pt1, 2, (0, 0, 255), -1)
# cv2.circle(img, pt2, 2, (0, 0, 255), -1)
# cv2.circle(img, pt3, 2, (0, 0, 255), -1)


# right click to draw circle

# def draw_circle(event, x, y, flags, params):
#     if event == cv2.EVENT_RBUTTONDOWN:
#         cv2.circle(img, (x, y), 200, (0, 0, 255), 10)


# cv2.namedWindow('circle')
# cv2.setMouseCallback('circle', draw_circle)

# while True:
# plt.imshow('circle', img)
# plt.show()
#     cv2.imshow('circle', img)
#     if cv2.waitKey(200) & 0xFF == 27:
#         break
# cv2.destroyAllWindows()
