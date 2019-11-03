import cv2
import matplotlib.pylab as plt
# 1. connect opencv to a WebCam
cap = cv2.VideoCapture(0)
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
frame = int(cap.get(cv2.CAP_PROP_FPS))
frame = int(cap.get(cv2.capprop))
colors = ('g', 'b', 'r')
# fourcc is 4-byte code used to specify the video codec,
#  XVID for linux
# DIVX for window
# writer = cv2.VideoWriter(
#     'myVideo.mp4',
#     cv2.VideoWriter_fourcc(*'XVID'),
#     10,  # img speed
#     (width, height))

print(width, height, frame)

while True:
    # read all cap to frame

    ret, frame = cap.read()

    # histogram

    # for i, col in enumerate(colors):
    #     hist = cv2.calcHist([frame], [i], None, [256], [0, 256])
    #     plt.plot(hist, color=col)

    #####################################

    # operations (drawing)
    # writer.write(frame)

    # gray = cv2.cvtColor(src=frame, code=cv2.COLOR_BGR2GRAY)

    cv2.imshow('frame', frame)
    cv2.imwrite('hello.jpg',frame[:,:])

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
# writer.release()
cv2.destroyAllWindows()
plt.show()
