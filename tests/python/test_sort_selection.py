import os
import sys
import unittest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))
from questions.python.sort_selection import Solution


class Test(unittest.TestCase):
    def test_selection_sort(self):
        self.assertEqual(
            Solution().selection_sort([8, 5, 2, 9, 5, 6, 3]), [2, 3, 5, 5, 6, 8, 9]
        )


if __name__ == "__main__":
    unittest.main()
