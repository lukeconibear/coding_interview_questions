import os
import sys
import unittest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
from questions.python.binary_search_tree_min_height import Node, Solution

def in_order_traverse(head, result): # time O(n), space O(n)
    if head is not None:
        in_order_traverse(head.left, result)
        result.append(head.value)
        in_order_traverse(head.right, result)

    return result

def validate_bst(head): # time O(n), space O(d)
    return validate_bst_helper(head, float('-inf'), float('inf'))

def validate_bst_helper(head, min_value, max_value):
    if head is None:
        return True

    if head.value < min_value or head.value >= max_value:
        return False

    is_left_valid = validate_bst_helper(head.left, min_value, head.value)
    is_right_valid = validate_bst_helper(head.right, head.value, max_value)
    return is_left_valid and is_right_valid

def get_height(head, height=0): # time O(d), space O(1)
    if head is None:
        return height

    left_height = get_height(head.left, height + 1)
    right_height = get_height(head.right, height + 1)
    return max(left_height, right_height)


class Test(unittest.TestCase):
    def test_min_height(self):
        head = Solution().construct_min_height_binary_search_tree([1, 2, 5, 7, 10, 13, 14, 15, 22])
        self.assertEqual(validate_bst(head), True)
        self.assertEqual(get_height(head), 4)
        self.assertEqual(in_order_traverse(head, []), [1, 2, 5, 7, 10, 13, 14, 15, 22])


if __name__ == '__main__':
    unittest.main()
