import os
import sys
import unittest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
from questions.python import two_sum


class Test(unittest.TestCase):
    def test_two_sum_naive(self):
        result = two_sum.Solution().two_sum_brute_force([3, 5, -4, 8, 11, 1, -1, 6], 10)
        self.assertTrue(result == [4, 6] or result == [6, 4])

    def test_two_sum_cache(self):
        result = two_sum.Solution().two_sum_cache([3, 5, -4, 8, 11, 1, -1, 6], 10)
        self.assertTrue(result == [4, 6] or result == [6, 4])


if __name__ == '__main__':
    unittest.main()
