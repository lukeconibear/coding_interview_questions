import os
import sys
import unittest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))
from questions.python.palindrome_check import Solution


class Test(unittest.TestCase):
    def test_is_palindrome(self):
        self.assertEqual(Solution().is_palindrome("abcdcba"), True)


if __name__ == "__main__":
    unittest.main()
