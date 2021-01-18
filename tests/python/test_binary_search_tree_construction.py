import os
import sys
import unittest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
from questions.python.binary_search_tree_construction import Node


class Test(unittest.TestCase):
    def test_binary_search_tree(self):
        head = Node(10)
        head.left = Node(5)
        head.left.left = Node(2)
        head.left.left.left = Node(1)
        head.left.right = Node(5)
        head.right = Node(15)
        head.right.left = Node(13)
        head.right.left.right = Node(14)
        head.right.right = Node(22)

        head.insert(12)
        self.assertTrue(head.right.left.left.value == 12)

        head.remove(10)
        self.assertTrue(not head.contains(10))
        self.assertTrue(head.value == 12)

        self.assertTrue(head.contains(15))


if __name__ == '__main__':
    unittest.main()
