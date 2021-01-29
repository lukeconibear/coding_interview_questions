import os
import sys
import unittest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
from questions.python.phone_number_nmemonics import Solution


class Test(unittest.TestCase):
    def test_phone_number_mnemonics(self):
        self.assertEqual(Solution().phone_number_mnemonics('1905'), ["1w0j", "1w0k", "1w0l", "1x0j", "1x0k", "1x0l", "1y0j", "1y0k", "1y0l", "1z0j", "1z0k", "1z0l"])


if __name__ == '__main__':
    unittest.main()
