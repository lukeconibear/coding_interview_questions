import os
import sys
import unittest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
from questions.python.binary_tree_branch_sums import Node, Solution


class Test(unittest.TestCase):
    def test_branch_sums(self):
        head = Node(1)
        head.left = Node(2)
        head.right = Node(3)
        head.left.left = Node(4)
        head.left.right = Node(5)
        head.left.left.left = Node(8)
        head.left.left.right = Node(9)
        head.left.right.left = Node(10)
        head.right.left = Node(6)
        head.right.right = Node(7)
        self.assertEqual(Solution().branch_sums(head), [15, 16, 18, 10, 11])


if __name__ == '__main__':
    unittest.main()
