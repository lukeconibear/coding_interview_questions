import os
import sys
import unittest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
from questions.python.binary_tree_diameter import Node, Solution


class Test(unittest.TestCase):
    def test_get_diameter(self):
        head = Node(1)
        head.left = Node(3)
        head.left.left = Node(7)
        head.left.left.left = Node(8)
        head.left.left.left.left = Node(9)
        head.left.right = Node(4)
        head.left.right.right = Node(5)
        head.left.right.right.right = Node(6)
        head.right = Node(2)

        self.assertEqual(Solution().get_diameter(head), 6)


if __name__ == '__main__':
    unittest.main()
