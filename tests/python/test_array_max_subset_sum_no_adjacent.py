import os
import sys
import unittest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
from questions.python.array_max_subset_sum_no_adjacent import Solution


class Test(unittest.TestCase):
    def test_max_subset_sum_no_adjacent(self):
        self.assertEqual(Solution().max_subset_sum_no_adjacent([75,105,120,75,90,135]), 330)


if __name__ == '__main__':
    unittest.main()
