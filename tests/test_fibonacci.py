import os
import sys
import unittest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from questions import fibonacci


class TestCalc(unittest.TestCase):
    def test_fib_recursive_brute_force(self):
        self.assertEqual(fibonacci.Solution().fib_recursive_brute_force(6), 5)
        self.assertEqual(fibonacci.Solution().fib_recursive_brute_force(10), 34)

    def test_fib_recursive_cached(self):
        self.assertEqual(fibonacci.Solution().fib_recursive_cached(6), 5)
        self.assertEqual(fibonacci.Solution().fib_recursive_cached(10), 34)

    def test_fib_iterative(self):
        self.assertEqual(fibonacci.Solution().fib_iterative(6), 5)
        self.assertEqual(fibonacci.Solution().fib_iterative(10), 34)


if __name__ == '__main__':
    unittest.main()
