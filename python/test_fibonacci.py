import unittest
import fibonacci


class TestCalc(unittest.TestCase):
    def test_add(self):
        self.assertEqual(fibonacci.fib_recursive(6), 5)
        self.assertEqual(fibonacci.fib_recursive(10), 55)

        self.assertEqual(fibonacci.fib_iterative(6), 5)
        self.assertEqual(fibonacci.fib_iterative(10), 55)


if __name__ == '__main__':
    unittest.main()
