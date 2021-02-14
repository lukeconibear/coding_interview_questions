import os
import sys
import unittest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))
from questions.python.array_class_photos import Solution


class Test(unittest.TestCase):
    def test_class_photos(self):
        self.assertEqual(
            Solution().class_photos([5, 8, 1, 3, 4], [6, 9, 2, 4, 5]), True
        )


if __name__ == "__main__":
    unittest.main()
