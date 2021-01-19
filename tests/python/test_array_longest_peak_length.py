import os
import sys
import unittest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
from questions.python.array_longest_peak_length import Solution


class Test(unittest.TestCase):
    def test_longest_peak_length(self):
        self.assertEqual(Solution().longest_peak_length([1, 2, 3, 3, 4, 0, 10, 6, 5, -1, -3, 2, 3]), 6)


if __name__ == '__main__':
    unittest.main()
