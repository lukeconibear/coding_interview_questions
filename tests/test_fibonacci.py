import unittest
from questions import fibonacci


class TestCalc(unittest.TestCase):
    def test_fib_recursive(self):
        self.assertEqual(fibonacci.fib_recursive(6), 5)
        self.assertEqual(fibonacci.fib_recursive(10), 34)

    def test_fib_iterative(self):
        self.assertEqual(fibonacci.fib_iterative(6), 5)
        self.assertEqual(fibonacci.fib_iterative(10), 34)


if __name__ == '__main__':
    unittest.main()
