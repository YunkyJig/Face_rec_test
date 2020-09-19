# Face_Recognition using openCV-python, dlib and face_recognition
 Using python face_recognition package and openCV for face detection of Jurassic Park characters.

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

## Contributing
Pull requests are welcome. As I'm also in the learning phase, any review or change will be appreciated. Also be sure to raise a issue for any change.

## License
[Apache License 2.0](https://choosealicense.com/licenses/apache-2.0/)
