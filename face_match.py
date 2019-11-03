import face_recognition

image_of_dane = face_recognition.load_image_file('./Images/dane.png')
dane_face_encoding = face_recognition.face_encodings(image_of_dane)[0]

unknow_image = face_recognition.load_image_file('./Images/jack_ma.jpg')
unknow_face_encoding = face_recognition.face_encodings(unknow_image)[0]

#compare image

results = face_recognition.compare_faces([dane_face_encoding],unknow_face_encoding, 0.6)
if results[0]:
    print('This is Dane')
else:
    print('This is not Dane')
