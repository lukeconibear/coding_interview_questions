import os
import sys
import unittest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
from questions.python.string_run_length_encoding import Solution


class Test(unittest.TestCase):
    def test_run_length_encoding(self):
        self.assertTrue(Solution().run_length_encoding("AAAAAAAAAAAAABBCCCCDD"), "9A4A2B4C2D")


if __name__ == '__main__':
    unittest.main()
