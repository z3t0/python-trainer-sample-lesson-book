import unittest
import lesson

class LessonTest(unittest.TestCase):
    def test_y_is_five(self):
        "Checking that y is equal to 5"
        self.assertEqual(lesson.y, 5)

    def test_x_is_five(self):
        "Checking that x is equal to 5"
        self.assertEqual(lesson.x, 5)

def main():
    unittest.main()

if __name__ == '__main__':
    unittest.main()
