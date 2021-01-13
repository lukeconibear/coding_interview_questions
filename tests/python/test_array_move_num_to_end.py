import os
import sys
import unittest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
from questions.python.array_move_num_to_end import Solution


class Test(unittest.TestCase):
    def test_move_num_to_end(self):
        self.assertTrue(Solution().move_num_to_end([2, 1, 2, 2, 2, 3, 4, 2], 2), [4, 1, 3, 2, 2, 2, 2, 2])


if __name__ == '__main__':
    unittest.main()
