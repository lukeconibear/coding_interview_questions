class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


class Solution:
    def validate_bst(self, head):  # time O(n), space O(d)
        return self.validate_bst_helper(head, float("-inf"), float("inf"))

    def validate_bst_helper(self, head, min_value, max_value):
        if head is None:
            return True

        if head.value < min_value or head.value >= max_value:
            return False

        is_left_valid = self.validate_bst_helper(head.left, min_value, head.value)
        is_right_valid = self.validate_bst_helper(head.right, head.value, max_value)
        return is_left_valid and is_right_valid
