class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __repr__(self):
        result = f'{self.value}'
        result += f'-{self.left}' if self.left else '-None'
        result += f'-{self.right}' if self.right else '-None'
        return result

class Solution:
    def construct_min_height_binary_search_tree(self, array): # time O(n), space O(n)
        return self.construct_min_height_binary_search_tree_helper(array, 0, len(array) - 1) # array is in sorted order

    def construct_min_height_binary_search_tree_helper(self, array, start_index, end_index):
        if start_index > end_index:
            return None

        middle_index = (start_index + end_index) // 2
        binary_search_tree = Node(array[middle_index])
        binary_search_tree.left = self.construct_min_height_binary_search_tree_helper(array, start_index, middle_index - 1)
        binary_search_tree.right = self.construct_min_height_binary_search_tree_helper(array, middle_index + 1, end_index)
        return binary_search_tree
