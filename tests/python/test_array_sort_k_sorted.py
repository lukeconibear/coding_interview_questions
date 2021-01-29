import os
import sys
import unittest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
from questions.python.array_sort_k_sorted import Solution, MinHeap


class Test(unittest.TestCase):
    def test_sort_k_sorted(self):
        self.assertEqual(Solution().sort_k_sorted([3, 2, 1, 5, 4, 7, 6, 5], 3), [1, 2, 3, 4, 5, 5, 6, 7])


if __name__ == '__main__':
    unittest.main()
