import os
import sys
import unittest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))
from questions.python.array_find_three_largest_numbers import Solution


class Test(unittest.TestCase):
    def test_find_three_largest_numbers_sort(self):
        self.assertEqual(
            Solution().find_three_largest_numbers_sort(
                [141, 1, 17, -7, -17, -27, 18, 541, 8, 7, 7]
            ),
            [18, 141, 541],
        )

    def test_find_three_largest_numbers_no_sort(self):
        self.assertEqual(
            Solution().find_three_largest_numbers_no_sort(
                [141, 1, 17, -7, -17, -27, 18, 541, 8, 7, 7]
            ),
            [18, 141, 541],
        )


if __name__ == "__main__":
    unittest.main()
