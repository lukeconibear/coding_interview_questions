class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


class Solution:
    def find_successor(self, array, node):  # time O(n), space O(n)
        order = self.in_order_traversal(array, [])
        for index, current_node in enumerate(order):
            if current_node == node and index < len(order) - 1:
                return order[index + 1]

    def in_order_traversal(self, node, result):  # time O(n), space O(n)
        if node is not None:
            self.in_order_traversal(node.left, result)
            result.append(node.value)
            self.in_order_traversal(node.right, result)

        return result
