import os
import sys
import unittest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))
from questions.python.depth_first_search import Node


class Test(unittest.TestCase):
    def test_depth_first_search(self):
        head = Node("A")
        head.add_child("B").add_child("C").add_child("D")
        head.children[0].add_child("E").add_child("F")
        head.children[2].add_child("G").add_child("H")
        head.children[0].children[1].add_child("I").add_child("J")
        head.children[2].children[0].add_child("K")
        self.assertEqual(
            head.depth_first_search([]),
            ["A", "B", "E", "F", "I", "J", "C", "D", "G", "K", "H"],
        )


if __name__ == "__main__":
    unittest.main()
