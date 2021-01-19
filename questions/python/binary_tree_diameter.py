class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


class TreeInfo:
    def __init__(self, height, diameter):
        self.height = height
        self.diameter = diameter


class Solution:
    def get_diameter(self, head): # time O(n), space O(d)
        return self.get_tree_info(head).diameter

    def get_tree_info(self, head): 
        if head is None:
            return TreeInfo(0, 0)

        left_info = self.get_tree_info(head.left)
        right_info = self.get_tree_info(head.right)

        longest_path_through_root = left_info.height + right_info.height
        max_diameter_so_far = max(left_info.diameter, right_info.diameter)
        current_diameter = max(longest_path_through_root, max_diameter_so_far)
        current_height = 1 + max(left_info.height, right_info.height)

        return TreeInfo(current_height, current_diameter)
        