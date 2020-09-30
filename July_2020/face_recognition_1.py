import face_recognition
image_of_abbi = face_recognition.load_image_file('./img/unknown/abbis.jpg')
face_landmarks_list = face_recognition.face_landmarks(image_of_abbi)
my_face_encoding = face_recognition.face_encodings(image_of_abbi)[0]
test_image = face_recognition.load_image_file('./img/groups/abbi.jpg')
test_face_encoding = face_recognition.face_encodings(test_image)[0]
results = face_recognition.compare_faces(
    [my_face_encoding], test_face_encoding)

if results[0]:
    print('This is ME.....')
else:
    print('This is Not  Me')


print(face_landmarks_list)