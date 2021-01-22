import os
import sys
import unittest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
from questions.python.array_task_assignment import Solution


class Test(unittest.TestCase):
    def test_task_assignment(self):
        self.assertEqual(Solution().task_assignment(3, [1, 3, 5, 3, 1, 4]), [[4, 2], [0, 5], [3, 1]])


if __name__ == '__main__':
    unittest.main()
