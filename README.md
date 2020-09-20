# Face_Recognition using openCV-python, dlib and face_recognition
Using python face_recognition package and openCV for face detection of Jurassic Park characters. The project is influenced by this wonderful [tutorial](https://www.pyimagesearch.com/2018/06/18/face-recognition-with-opencv-python-and-deep-learning/) on Face Recognition with openCV and Deep learning by [Adrian Rosebrock](https://github.com/jrosebr1).

Also, this is just a learning project and the code is not being used by me for any monetary or tutorial purposes. 

## For generating the encodings file:
run 
```bash
python encode_face.py --dataset dataset --encodings encodings.pickle
```
in the terminal with the right directory and environment activated.

## For running the face recognition script:
run  
```bash 
python recognize_faces_image.py --encodings encodings.pickle --image examples/example_1.jpg
```

## Examples
![alt text](https://github.com/GhostUser/Jurassic-Park-characters-Face-recognition/blob/master/Sample_1.jpg)

## Requirements
The following libraries and packages should be installed in the virtual environment:
* face_recognition(Adam Geitgey)
* dlib (maintained by Davis King)
* openCV-python
* imutils
* agrparse

Packages can be installed by using package manager [pip](https://pip.pypa.io/en/stable/).
```bash
pip install <package_name>
```

* Before installing the dlib, make sure you have [CMake](https://cmake.org/) installed on your system.

## Dataset 
All images for dataset and examples are collected by me using a chrome extension, which can be downloaded from [here](https://chrome.google.com/webstore/detail/ifipmflagepipjokmbdecpmjbibjnakm).

## License
[PyImageSerch](https://www.pyimagesearch.com/faqs/single-faq/what-is-the-code-license-associated-with-your-examples/)


## Reference 
A major part of project is taken from a blog by [Adrian Rosebrock](https://github.com/jrosebr1) on [PyimageSearch](https://www.pyimagesearch.com/).

The referenced tutorial on Face Recognition with openCV and Deep Learning can be found [here](https://www.pyimagesearch.com/).
