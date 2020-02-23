import face_recognition
from PIL import Image


def compare(img_1_filepath, img_2_filepath):

    known_image = face_recognition.load_image_file(img_1_filepath)
    unknown_image = face_recognition.load_image_file(img_2_filepath)

    img_1_encoding = face_recognition.face_encodings(
        known_image)
    if len(img_1_encoding) == 0:
        return "No face"
    else:
        img_1_encoding = img_1_encoding[0]

    img_2_encoding = face_recognition.face_encodings(
        unknown_image)
    if len(img_2_encoding) == 0:
        return "No face"
    else:
        img_2_encoding = img_2_encoding[0]

    results = face_recognition.compare_faces(
        [img_1_encoding], img_2_encoding, tolerance=0.75)

    return results
