from imutils import paths
import face_recognition
import pickle
import cv2
import os

directory = "D:\\Dataset\\"
if not os.path.exists(directory):
    os.makedirs(directory)

print("[INFO] quantifying faces...")
imagePaths = list(paths.list_images("D:\\Dataset\\"))
knownEncodings = []
knownNames = []

for (i, imagePath) in enumerate(imagePaths):
    print("[INFO] processing image {}/{}".format(i + 1,
                                                 len(imagePaths)))

    try:
        f = open("D:\\Training_Status.txt", "w")
        f.write("{}|{}".format(i + 1, len(imagePaths)))
        f.close()
    except Exception as e:
        pass

    name = imagePath.split(os.path.sep)[-2]
    image = cv2.imread(imagePath)
    rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    boxes = face_recognition.face_locations(rgb, model="hog")
    encodings = face_recognition.face_encodings(rgb, boxes)
    for encoding in encodings:
        knownEncodings.append(encoding)
        knownNames.append(name)

print("[INFO] serializing encodings...")
data = {"encodings": knownEncodings, "names": knownNames}
f = open("D:\\TrainingModels\\Model.pickle", "wb")
f.write(pickle.dumps(data))
f.close()