import os
import sys
import unittest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
from questions.python.array_non_constructible_change import Solution


class Test(unittest.TestCase):
    def test_non_constructible_change(self):
        self.assertEqual(Solution().non_constructible_change([5, 7, 1, 1, 2, 3, 22]), 20)


if __name__ == '__main__':
    unittest.main()
