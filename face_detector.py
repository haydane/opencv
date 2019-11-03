import face_recognition

image = face_recognition.load_image_file('./Images/abba.png')
face_locations = face_recognition.face_locations(image);

print(face_locations)
print(f'there are {len(face_locations)} people in this image')