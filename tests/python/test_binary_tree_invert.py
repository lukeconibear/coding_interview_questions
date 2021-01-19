import os
import sys
import unittest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
from questions.python.binary_tree_invert import Node, Solution


class Test(unittest.TestCase):
    def test_invert_binary_tree(self):
        head = Node(1)
        head.left = Node(2)
        head.left.left = Node(4)
        head.left.right = Node(5)
        head.left.left.left = Node(8)
        head.left.left.right = Node(9)
        head.right = Node(3)
        head.right.left = Node(6)
        head.right.right = Node(7)

        inverted_head = Node(1)
        inverted_head.left = Node(3)
        inverted_head.left.left = Node(7)
        inverted_head.left.right = Node(6)
        inverted_head.right = Node(2)
        inverted_head.right.left = Node(5)
        inverted_head.right.right = Node(4)
        inverted_head.right.right.left = Node(9)
        inverted_head.right.right.right = Node(8)

        actual_result = str(Solution().invert_binary_tree(head))
        expected_result = str(inverted_head)

        self.assertEqual(actual_result, expected_result)


if __name__ == '__main__':
    unittest.main()
