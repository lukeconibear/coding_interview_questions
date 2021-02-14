import os
import sys
import unittest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))
from questions.python.array_is_monotonic import Solution


class Test(unittest.TestCase):
    def test_is_monotonic(self):
        self.assertEqual(
            Solution().is_monotonic([-1, -5, -10, -1100, -1100, -1101, -1102, -9001]),
            True,
        )


if __name__ == "__main__":
    unittest.main()
