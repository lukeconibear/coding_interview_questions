class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


class Solution:
    def in_order_traversal(self, head, result): # time O(n), space O(n)
        if head is not None:
            self.in_order_traversal(head.left, result)
            result.append(head.value)
            self.in_order_traversal(head.right, result)

        return result

    def pre_order_traversal(self, head, result): # time O(n), space O(n)
        if head is not None:
            result.append(head.value)
            self.pre_order_traversal(head.left, result)
            self.pre_order_traversal(head.right, result)

        return result

    def post_order_traversal(self, head, result): # time O(n), space O(n)
        if head is not None:
            self.post_order_traversal(head.left, result)
            self.post_order_traversal(head.right, result)
            result.append(head.value)

        return result
