import os
import sys
import unittest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
from questions.python.array_minimum_waiting_time import Solution


class Test(unittest.TestCase):
    def test_minimum_waiting_time(self):
        self.assertEqual(Solution().minimum_waiting_time([3, 2, 6, 2, 1]), 17)


if __name__ == '__main__':
    unittest.main()
