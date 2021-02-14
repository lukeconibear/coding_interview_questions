import os
import sys
import unittest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))
from questions.python.array_three_sum import Solution


class Test(unittest.TestCase):
    def test_three_number_sum(self):
        self.assertEqual(
            Solution().three_number_sum([12, 3, 1, 2, -6, 5, -8, 6], 0),
            [[-8, 2, 6], [-8, 3, 5], [-6, 1, 5]],
        )


if __name__ == "__main__":
    unittest.main()
