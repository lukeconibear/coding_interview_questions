import unittest
import fibonacci


class TestCalc(unittest.TestCase):
    def test_add(self):
        result = fibonacci.get_nth_fib(6)
        self.assertEqual(result, 5)


if __name__ == '__main__':
    unittest.main()
