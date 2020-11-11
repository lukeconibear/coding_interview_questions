import os
import sys
import unittest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from questions.two_sum import Solution


class Test(unittest.TestCase):
    def test_two_sum_naive(self):
        result = Solution().two_sum_naive([3, 5, -4, 8, 11, 1, -1, 6], 10)
        self.assertTrue(result == [4, 6] or result == [6, 4])

    def test_two_sum_cache(self):
        result = Solution().two_sum_cache([3, 5, -4, 8, 11, 1, -1, 6], 10)
        self.assertTrue(result == [4, 6] or result == [6, 4])


if __name__ == '__main__':
    unittest.main()
