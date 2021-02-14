import os
import sys
import unittest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))
from questions.python.array_spiral_traverse import Solution


class Test(unittest.TestCase):
    def test_spiral_traverse(self):
        self.assertEqual(
            Solution().spiral_traverse(
                [[1, 2, 3, 4], [12, 13, 14, 5], [11, 16, 15, 6], [10, 9, 8, 7]]
            ),
            [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16],
        )


if __name__ == "__main__":
    unittest.main()
