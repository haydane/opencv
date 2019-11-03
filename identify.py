import face_recognition
from PIL import Image,ImageDraw
import cv2 

image_of_stevejob = face_recognition.load_image_file('./Images/steve_job.jpg')
stevejob_face_encoding = face_recognition.face_encodings(image_of_stevejob)[0]

image_of_jackma = face_recognition.load_image_file('./Images/jack_ma.jpg')
jackma_face_encoding = face_recognition.face_encodings(image_of_jackma)[0]

image_of_billgate = face_recognition.load_image_file('./Images/billgate.jpg')
billgate_face_encoding = face_recognition.face_encodings(image_of_billgate)[0]

image_of_dane = face_recognition.load_image_file('./Images/dane1.png')
dane_face_encoding = face_recognition.face_encodings(image_of_dane)[0]


# create array of encodings and name
known_face_encodings = [
    stevejob_face_encoding,
    jackma_face_encoding,
    billgate_face_encoding,
    dane_face_encoding
]

known_face_names = [
    "Steve Job",
    "Jack Ma",
    "Bill Gate",
    "Hay Dane"
]

# load test image to find faces in
test_image = face_recognition.load_image_file('./Images/dane2.png')

# Find faces in test image
face_locations = face_recognition.face_locations(test_image)
face_encodings = face_recognition.face_encodings(test_image, face_locations)

# covert to PIL image
pil_image = Image.fromarray(test_image)

#create a ImageDraw instance 
draw = ImageDraw.Draw(pil_image)

# loop through faces in test image
for(top,right,bottom,left), face_encoding in zip(face_locations,face_encodings):
    matches = face_recognition.compare_faces(known_face_encodings,face_encoding)
    name = "Uknown Person"

    # if match
    if True in matches:
        first_match_index = matches.index(True)
        name = known_face_names[first_match_index]
    
    #Draw box
    draw.rectangle(((left,top),(right,bottom)),outline=(255,255,0))

    #draw label
    text_width, text_height = draw.textsize(name)
    draw.rectangle(((left,bottom - text_height - 10), (right, bottom)), fill=(255,255,0), outline=(255,255,0))
    draw.text((left + 6, bottom - text_height - 5), name, fill=(0,0,0))

del draw
#display image
pil_image.show()