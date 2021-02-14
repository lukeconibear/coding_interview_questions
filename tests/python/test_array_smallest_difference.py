import os
import sys
import unittest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))
from questions.python.array_smallest_difference import Solution


class Test(unittest.TestCase):
    def test_find_smallest_difference(self):
        self.assertEqual(
            Solution().find_smallest_difference(
                [-1, 5, 10, 20, 28, 3], [26, 134, 135, 15, 17]
            ),
            [28, 26],
        )


if __name__ == "__main__":
    unittest.main()
