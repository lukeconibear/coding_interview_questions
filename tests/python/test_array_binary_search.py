import os
import sys
import unittest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))
from questions.python.array_binary_search import Solution


class Test(unittest.TestCase):
    def test_binary_search_recursive(self):
        self.assertEqual(
            Solution().binary_search_recursive(
                [0, 1, 21, 33, 45, 45, 61, 71, 72, 73], 33
            ),
            3,
        )

    def test_binary_search_iterative(self):
        self.assertEqual(
            Solution().binary_search_iterative(
                [0, 1, 21, 33, 45, 45, 61, 71, 72, 73], 33
            ),
            3,
        )


if __name__ == "__main__":
    unittest.main()
