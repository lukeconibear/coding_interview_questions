import os
import sys
import unittest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))
from questions.python.binary_search_tree_traversal import Node, Solution


class Test(unittest.TestCase):
    def test_traversal(self):
        head = Node(10)
        head.left = Node(5)
        head.left.left = Node(2)
        head.left.left.left = Node(1)
        head.left.right = Node(5)
        head.right = Node(15)
        head.right.right = Node(22)

        self.assertEqual(
            Solution().in_order_traversal(head, []), [1, 2, 5, 5, 10, 15, 22]
        )
        self.assertEqual(
            Solution().pre_order_traversal(head, []), [10, 5, 2, 1, 5, 15, 22]
        )
        self.assertEqual(
            Solution().post_order_traversal(head, []), [1, 2, 5, 5, 22, 15, 10]
        )


if __name__ == "__main__":
    unittest.main()
