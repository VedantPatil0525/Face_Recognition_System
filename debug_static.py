import face_recognition

image = face_recognition.load_image_file("dataset/Anaya/photo1.jpeg")
boxes = face_recognition.face_locations(image)

print("Faces found:", len(boxes))
print(image.dtype, image.shape)
