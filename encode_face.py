from imutils import paths
import face_recognition
import argparse
import pickle
import cv2
import os

# construct the argument parser and parse the arguments
ap=argparse.ArgumentParser()
ap.add_argument("-i", "--dataset", required=True, help="path to input directory of faces + images")
ap.add_argument("-e", "--encodings", required=True, help="path to serialized db of facial encodings")
ap.add_argument("-d", "--detection-method", type=str, default="cnn", help="face detection model to use: either `hog` or `cnn`")
args= vars(ap.parse_args)

# grab the paths to the input images in our dataset
print("Quantifying faces...")
imagePaths = list(paths.list_images("dataset"))
# initialize the list of known encodings and known names
knownEncodings = []
knownNames = []

#loop over the image paths
for (i, imagePath) in enumerate(imagePaths):
    print("Processing image {}/{}".format(i + 1, len(imagePaths)))
    name = imagePath.split(os.path.sep)[-2]


    image = cv2.imread(imagePath)
    rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    boxes= face_recognition.face_locations(rgb, model="detection_method")

    #compute the facial embedding for the face
    encodings=face_recognition.face_encodings(rgb, boxes)

    # loop over the encodings
    for encoding in encodings:
        knownEncodings.append(encoding)
        knownNames.append(name)

# Dump the facial encodings + names to disk
print("Serializing encodings.....")
data = {"encodings": knownEncodings, "names": knownNames}
f = open("encodings.pickle", "wb")
f.write(pickle.dumps(data))
f.close()
