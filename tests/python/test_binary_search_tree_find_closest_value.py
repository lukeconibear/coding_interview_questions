import os
import sys
import unittest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))
from questions.python.binary_search_tree_find_closest_value import Solution, Node


class TestCalc(unittest.TestCase):
    def test_is_valid_subsequence_iterative(self):
        head = Node(10)
        head.left = Node(5)
        head.left.left = Node(2)
        head.left.right = Node(5)
        head.left.left.left = Node(1)
        head.right = Node(15)
        head.right.left = Node(13)
        head.right.right = Node(22)
        head.right.left.right = Node(14)
        self.assertEqual(
            Solution().binary_search_tree_find_closest_value_iterative(head, 12), 13
        )

    def test_is_valid_subsequence_recursive(self):
        head = Node(10)
        head.left = Node(5)
        head.left.left = Node(2)
        head.left.right = Node(5)
        head.left.left.left = Node(1)
        head.right = Node(15)
        head.right.left = Node(13)
        head.right.right = Node(22)
        head.right.left.right = Node(14)
        self.assertEqual(
            Solution().binary_search_tree_find_closest_value_recursive(head, 12), 13
        )


if __name__ == "__main__":
    unittest.main()
