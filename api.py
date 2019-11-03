import cv2
import numpy as np
import requests

faceCascade = cv2.CascadeClassifier('./cascade/haarcascade_frontalface_default.xml')


cap = cv2.VideoCapture(0);
while True:
    ret, frame = cap.read();
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(gray,scaleFactor=1.4,minNeighbors=1,minSize=(10,10))
    for x,y,w,h in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
        print(faces)
    cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cap.destroyAllWindows()

# pay_load = {'msg': 'hello'}
# requests.post('http://192.168.11.43:3000/ut-blockchain', json={'msg': 'hello'});
# requests.post('http://192.168.11.43:3000/ut-blockchain', data='hello');