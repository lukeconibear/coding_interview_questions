class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __repr__(self):
        result = f"{self.value}"
        result += f"-{self.left}" if self.left else "-None"
        result += f"-{self.right}" if self.right else "-None"
        return result


class Solution:
    def invert_binary_tree(self, head):  # time O(n), space O(d)
        if head is None:
            return None

        head.left, head.right = head.right, head.left
        self.invert_binary_tree(head.left)
        self.invert_binary_tree(head.right)

        return head
