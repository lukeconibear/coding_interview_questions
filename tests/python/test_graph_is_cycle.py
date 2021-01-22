import os
import sys
import unittest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
from questions.python.graph_is_cycle import Solution


class Test(unittest.TestCase):
    def test_is_cycle(self):
        self.assertEqual(Solution().is_cycle([[1, 3], [2, 3, 4], [0], [], [2, 5], []]), True)


if __name__ == '__main__':
    unittest.main()
