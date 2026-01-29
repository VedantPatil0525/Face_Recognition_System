📘 Face Recognition System using OpenCV & Python

A real-time Face Recognition System built using Python, OpenCV, dlib, and face_recognition.
The system detects and recognizes multiple faces simultaneously from a live webcam feed and automatically terminates after successful recognition.

🚀 Features

Real-time face detection and recognition

Supports multiple faces in a single frame

Uses pre-trained deep learning face embeddings

Automatically closes after detecting a known face (with delay)

Works efficiently on CPU (no GPU required)

Modular and easy-to-extend architecture

🖼️ Demo Screenshot

![Face Recognition Demo](Screenshots/Output1.png)

The system recognizing Vedant and Anaya simultaneously in real time.

🧠 How It Works (Concept)

1. Face Detection
Detects faces from images or live webcam frames using dlib’s HOG-based detector.

2. Face Encoding
Each detected face is converted into a 128-dimensional numerical embedding that uniquely represents facial features.

3. Face Matching
The live face encodings are compared with stored encodings using Euclidean distance.
If the distance is below a threshold, the face is recognized.

🗂️ Project Structure

Face_Recognition_System/

│

├── dataset/

│ ├── Vedant/

│ │ ├── image1.jpg

│ │ ├── image2.jpg

│ │ └── image3.jpg

│ │

│ └── Anaya/

│ ├── image1.jpg

│ └── image2.jpg

│

├── screenshots/

│ └── output1.png

│

├── encode_faces.py

├── recognize_faces.py

├── debug_static.py

├── encodings.pickle

└── README.md


🛠️ Technologies Used

- Python 3.9

- OpenCV

- dlib

- face_recognition

- NumPy

- Pillow

⚙️ Setup Instructions

1️⃣ Create Conda Environment

conda create -n face_recog python=3.9

conda activate face_recog

2️⃣ Install Dependencies

conda install -c conda-forge dlib

pip install face-recognition opencv-python pillow numpy

▶️ How to Run the Project

Step 1: Encode Faces

python encode_faces.py

Step 2: Run Face Recognition

python recognize_faces.py

Press q to exit manually

Or the system auto-closes 10 seconds after detection

🎯 Use Cases

- Attendance Management System

- Access Control Systems

- Identity Verification

- Smart Surveillance

- Academic & Research Projects

⚠️ Limitations

- Performance depends on lighting conditions

- Accuracy may reduce with occlusion (masks, caps)

- Not designed for large-scale datasets

🔮 Future Enhancements

- Attendance logging with date & time (CSV)

- GUI using Tkinter or PyQt

- Database integration

- Web-based interface using Flask

- Face mask detection

- Emotion recognition

⭐ If you like this project

Give it a ⭐ on GitHub — it motivates further improvements!
