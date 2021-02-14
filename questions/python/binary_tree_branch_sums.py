class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


class Solution:
    def branch_sums(self, head):  # time O(n), space O(n)
        sums = []
        self.calculate_branch_sums(head, 0, sums)
        return sums

    def calculate_branch_sums(self, node, current_sum, sums):
        if node is None:
            return

        current_sum = current_sum + node.value
        if node.left is None and node.right is None:
            sums.append(current_sum)
            return

        self.calculate_branch_sums(node.left, current_sum, sums)
        self.calculate_branch_sums(node.right, current_sum, sums)
