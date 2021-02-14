import os
import sys
import unittest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))
from questions.python.array_of_products import Solution


class Test(unittest.TestCase):
    def test_products(self):
        self.assertEqual(Solution().products([5, 1, 4, 2]), [8, 40, 10, 20])


if __name__ == "__main__":
    unittest.main()
