import cv2
import matplotlib.pyplot as plt

cap = cv2.VideoCapture(0)


def canny_detection(img):
    # img = cv2.imread(img, 0)
    img = cv2.cvtColor(img, cv2.THRESH_BINARY)
    edges = cv2.Canny(img, 100, 200)
    return edges


while True:

    ret, frame = cap.read(0)

    frame = canny_detection(frame)
    cv2.imshow('Video Frame', frame)

    k = cv2.waitKey(1)
    if k == 27:
        break

# plt.subplot(121), plt.imshow(img, cmap='gray')

# plt.title('Before')

# plt.subplot(122), plt.imshow(edges, cmap='gray')
# plt.title('after')

# plt.suptitle('testing')
# plt.show()

cap.release()
cv2.destroyAllWindows()