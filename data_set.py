import numpy as np
import cv2
import os 
from PIL import Image

path = 'dataset'

recognizer = cv2.face_FaceRecognizer()

def getImageWithID(path):
    imagePaths = [os.path.join(path,f) for f in os.listdir(path)] 
    faces=[]
    ids=[]
    for imagePath in imagePaths:
        faceImage = Image.open(imagePath).convert('L')
        faceNp = np.array(faceImage,'uint8')
        ID = int(os.path.split(imagePath)[-1].split('.')[1])
        print(ID)
        faces.append(faceNp)
        ids.append(ID)
        cv2.imshow('training',faceNp)
        cv2.waitKey(5)
        return faces,ids


faces, ids = getImageWithID(path)
recognizer.train(faces,np.array(ids))
recognizer.save('recognizer/trainingData.yml')
cv2.destroyAllWindows()
# face_cascade = cv2.CascadeClassifier('./cascade/haarcascade_frontalface_default.xml')

# cap = cv2.VideoCapture(0)

# id = input('enter user id')

# sampleN=0;

# while 1:

#     ret, img = cap.read()

#     gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#     faces = face_cascade.detectMultiScale(gray, 1.3, 5)

#     for (x,y,w,h) in faces:

#         sampleN=sampleN+1;

#         cv2.imwrite("./dataset/"+str(id)+ "." +str(sampleN)+ ".jpg", gray[y:y+h, x:x+w])

#         cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)

#         cv2.waitKey(100)

#     cv2.imshow('img',img)

#     cv2.waitKey(1)

#     if sampleN > 20:

#         break

# cap.release()

# cv2.destroyAllWindows()