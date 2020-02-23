import unittest
from face_check import checkForFace
from face_compare import compare


class TestFaceRecognition(unittest.TestCase):

    def test_CheckForFace_1(self):
        self.assertEqual(checkForFace(
            "data/test_images/IMG_0507.jpg"), False)

    def test_CheckForFace_2(self):
        self.assertEqual(checkForFace(
            "data/test_images/female1.jpg"), True)

    def test_Compare_1(self):
        self.assertEqual(compare(
            "data/test_images/IMG_0507.jpg", "data/test_images/female1.jpg"), "No face")

    def test_Compare_2(self):
        self.assertEqual(compare(
            "data/test_images/female3.jpg", "data/test_images/female4.jpg"), [True])

    def test_Compare_3(self):
        self.assertEqual(compare(
            "data/test_images/female4.jpg", "data/test_images/female4.jpg"), [True])


if __name__ == '__main__':
    unittest.main()
