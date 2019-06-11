import cv2
import time
import matplotlib.pyplot as plt
cap = cv2.VideoCapture('./images/myVideo.mp4')


if cap.isOpened() == False:
    print('error file not found or wrong coded used')
while cap.isOpened():
    ret, frame = cap.read()

    if ret == True:
        time.sleep(1/10)
        cv2.imshow('frame', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break
cap.release()
