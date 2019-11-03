import cv2
import sys

imagePath = sys.argv[1]
cascPath = sys.argv[2]

faceCascade = cv2.CascadeClassifier(cascPath)

# Read Image
image = cv2.imread(imagePath)
gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

faces = faceCascade.detectMultiScale(
    gray,
    scaleFactor=1.2,
    minNeighbors=7,
    minSize=(30,30),
    flags=cv2.CASCADE_SCALE_IMAGE
)

for x,y,w,h in faces:
    cv2.rectangle(image,(x,y),(x+h,y+h),(0,255,0),5)

print("Found faces!" , format(len(faces)))
cv2.namedWindow("output",cv2.WINDOW_NORMAL)
imS = cv2.resize(image,(800,500))
cv2.imshow("Faces Found",imS)
cv2.waitKey(0)

