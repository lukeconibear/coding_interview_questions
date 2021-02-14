import os
import sys
import unittest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))
from questions.python.array_product_sum import Solution


class Test(unittest.TestCase):
    def test_product_sum(self):
        self.assertEqual(
            Solution().product_sum([5, 2, [7, -1], 3, [6, [-13, 8], 4]]), 12
        )


if __name__ == "__main__":
    unittest.main()
