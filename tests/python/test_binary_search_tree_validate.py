import os
import sys
import unittest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))
from questions.python.binary_search_tree_validate import Node, Solution


class Test(unittest.TestCase):
    def test_validate(self):
        head = Node(10)
        head.left = Node(5)
        head.left.left = Node(2)
        head.left.left.left = Node(1)
        head.left.right = Node(5)
        head.right = Node(15)
        head.right.left = Node(13)
        head.right.left.right = Node(14)
        head.right.right = Node(22)

        self.assertEqual(Solution().validate_bst(head), True)


if __name__ == "__main__":
    unittest.main()
