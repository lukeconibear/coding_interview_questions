import os
import sys
import unittest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
from questions.python.array_first_duplicate_value import Solution


class Test(unittest.TestCase):
    def test_first_duplicate_value(self):
        self.assertTrue(Solution().first_duplicate_value([2, 1, 5, 2, 3, 3, 4]), 2)


if __name__ == '__main__':
    unittest.main()
