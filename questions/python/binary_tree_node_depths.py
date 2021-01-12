class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

class Solution:
    def node_depths(self, node, depth=0): # time O(n), space O(h)
        if node is None:
            return 0
        return depth + self.node_depths(node.left, depth + 1) + self.node_depths(node.right, depth + 1)


