import cv2
import matplotlib.pyplot as plt
import numpy as np

# first image
img = cv2.imread('./images/flat_chess_board.png')
found, corners = cv2.findChessboardCorners(image=img, patternSize=(6, 6))
cv2.drawChessboardCorners(image=img, patternSize=(
    6, 6), corners=corners, patternWasFound=found)

# second image
dots = cv2.imread('./images/dots.jpg')
found, corners = cv2.findCirclesGrid(
    dots, (10, 10), cv2.CALIB_CB_ASYMMETRIC_GRID)
cv2.drawChessboardCorners(image=dots, patternSize=(
    10, 10), corners=corners, patternWasFound=found)
print(found, corners)
plt.imshow(dots)

plt.show()
