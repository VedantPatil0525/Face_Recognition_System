import face_recognition
import os
import pickle

dataset_path = "dataset"
known_encodings = []
known_names = []

for person_name in os.listdir(dataset_path):
    person_path = os.path.join(dataset_path, person_name)

    if not os.path.isdir(person_path):
        continue

    for image_name in os.listdir(person_path):
        image_path = os.path.join(person_path, image_name)

        image = face_recognition.load_image_file(image_path)
        encodings = face_recognition.face_encodings(image)

        if len(encodings) != 1:
            print(f"⚠️ Skipped {image_name}")
            continue

        known_encodings.append(encodings[0])
        known_names.append(person_name)

data = {
    "encodings": known_encodings,
    "names": known_names
}

with open("encodings.pickle", "wb") as f:
    pickle.dump(data, f)

print("✅ Encoding completed")
print("Total encodings:", len(known_encodings))
print("Keys saved in pickle:", data.keys())
