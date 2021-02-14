import os
import sys
import unittest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))
from questions.python.binary_tree_find_successor import Node, Solution


class Test(unittest.TestCase):
    def test_find_successor(self):
        head = Node(1)
        head.left = Node(2)
        head.right = Node(3)
        head.left.left = Node(4)
        head.left.right = Node(5)
        head.left.left.left = Node(6)

        self.assertEqual(Solution().find_successor(head, 5), 1)


if __name__ == "__main__":
    unittest.main()
