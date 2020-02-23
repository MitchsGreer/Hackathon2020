import unittest
import src.face_check
import src.face_compare


class TestFaceRecognition(unittest.TestCase):

    def test_CheckForFace_1(self):
        self.assertEqual(src.face_check.checkForFace(
            "data/test_images/IMG_0507.jpg"), False)

    def test_CheckForFace_2(self):
        self.assertEqual(src.face_check.checkForFace(
            "data/test_images/female1.jpg"), True)

    def test_Compare_1(self):
        self.assertEqual(src.face_compare.compare(
            "data/test_images/IMG_0507.jpg", "data/test_images/female1.jpg"), False)

    def test_Compare_2(self):
        self.assertEqual(src.face_compare.compare(
            "data/test_images/female3.jpg", "data/test_images/female4.jpg"), False)


if __name__ == '__main__':
    unittest.main()
