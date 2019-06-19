import cv2
import matplotlib.pyplot as plt
import numpy as np

# first image
chess = cv2.imread('../images/flat_chess_board.png')
chess = cv2.cvtColor(chess, cv2.COLOR_BGR2RGB)
found, corners = cv2.findChessboardCorners(image=chess, patternSize=(6, 6))
cv2.drawChessboardCorners(image=chess, patternSize=(
    6, 6), corners=corners, patternWasFound=found)

# second image
dots = cv2.imread('../images/dots.jpg')
found, corners = cv2.findCirclesGrid(
    dots, (10, 10), cv2.CALIB_CB_ASYMMETRIC_GRID)
cv2.drawChessboardCorners(image=dots, patternSize=(
    10, 10), corners=corners, patternWasFound=found)
print(found, corners)

plt.subplot(121)
plt.imshow(chess)
plt.title('Chess Board')

plt.subplot(122)
plt.imshow(dots)
plt.title('Dots')

plt.suptitle('Find Grid')
plt.show()
