import os
import sys
import unittest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))
from questions.python.array_is_valid_subsequence import Solution


class TestCalc(unittest.TestCase):
    def test_is_valid_subsequence(self):
        self.assertEqual(
            Solution().is_valid_subsequence(
                [5, 1, 22, 25, 6, -1, 8, 10], [1, 6, -1, 10]
            ),
            True,
        )
        self.assertEqual(
            Solution().is_valid_subsequence(
                [5, 1, 22, 25, 6, -1, 8, 10], [5, 1, 22, 25, 6, -1, 8, 10]
            ),
            True,
        )

    def test_is_valid_subsequence_alternative(self):
        self.assertEqual(
            Solution().is_valid_subsequence_alternative(
                [5, 1, 22, 25, 6, -1, 8, 10], [1, 6, -1, 10]
            ),
            True,
        )
        self.assertEqual(
            Solution().is_valid_subsequence_alternative(
                [5, 1, 22, 25, 6, -1, 8, 10], [5, 1, 22, 25, 6, -1, 8, 10]
            ),
            True,
        )


if __name__ == "__main__":
    unittest.main()
