import os
import sys
import unittest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
from questions.python.caesar_cipher_encryptor import Solution


class Test(unittest.TestCase):
    def test_caesar_cipher_encryptor(self):
        self.assertTrue(Solution().caesar_cipher_encryptor('xyz', 2), 'zab')


if __name__ == '__main__':
    unittest.main()
