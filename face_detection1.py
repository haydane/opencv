import cv2
import sys

# Get user supplied values
imagePath = sys.argv[1]
# cascPath = "haarcascade_frontalface_default.xml"

# Create the haar cascade
faceCascade = cv2.CascadeClassifier('../Document/Computer-Vision-with-Python/DATA/haarcascades/haarcascade_frontalface_default.xml')

# Read the image
image = cv2.imread(imagePath)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Detect faces in the image
faces = faceCascade.detectMultiScale(
    gray,
    # scaleFactor=1.1,
    scaleFactor=1.1,
    minNeighbors=5,
    minSize=(30, 30),
)

print("Found {0} faces!".format(len(faces)))

# Draw a rectangle around the faces
for (x, y, w, h) in faces:
    cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)
    roi_face = image[y:y+h,x:x+w]
    cv2.imwrite('pic.png',roi_face);

cv2.imshow("Faces found", image)
cv2.waitKey(0)