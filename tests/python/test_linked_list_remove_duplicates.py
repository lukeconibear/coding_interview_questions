import os
import sys
import unittest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
from questions.python.linked_list_remove_duplicates import Node, Solution


class Test(unittest.TestCase):
    def test_remove_duplicates(self):
        head = Node(1)
        head.next = Node(1)
        head.next.next = Node(3)
        head.next.next.next = Node(4)
        head.next.next.next.next = Node(4)
        head.next.next.next.next.next = Node(5)
        head.next.next.next.next.next.next = Node(6)
        head.next.next.next.next.next.next.next = Node(6)

        result = Node(1)
        result.next = Node(3)
        result.next.next = Node(4)
        result.next.next.next = Node(5)
        result.next.next.next.next = Node(6)

        self.assertEqual(print(Solution().remove_duplicates(head)), print(result))


if __name__ == '__main__':
    unittest.main()
