import cv2
import face_recognition
import os
import pickle

all_face_encodings = []
path = 'trainingImages'
myList = os.listdir(path)
images = []
print('encoding...')
for cl in myList:
    curImg = cv2.imread(f'{path}/{cl}')
    images.append(curImg)

for img in images:
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    encode = face_recognition.face_encodings(img)[0]
    all_face_encodings.append(encode)

with open('encodings.dat', 'wb') as f:
    pickle.dump(all_face_encodings, f)

print('success!')
print(all_face_encodings)