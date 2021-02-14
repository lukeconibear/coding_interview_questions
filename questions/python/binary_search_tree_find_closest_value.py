class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


class Solution:
    def binary_search_tree_find_closest_value_iterative(self, head, target):
        return self.binary_search_tree_find_closest_value_iterative_helper(
            head, target, head.value
        )

    def binary_search_tree_find_closest_value_iterative_helper(
        self, head, target, closest
    ):
        current_node = head
        while current_node is not None:
            if abs(target - closest) > abs(target - current_node.value):
                closest = current_node.value
            if target < current_node.value:
                current_node = current_node.left
            elif target > current_node.value:
                current_node = current_node.right
            else:
                break

        return closest

    def binary_search_tree_find_closest_value_recursive(self, head, target):
        return self.binary_search_tree_find_closest_value_recursive_helper(
            head, target, head.value
        )

    def binary_search_tree_find_closest_value_recursive_helper(
        self, head, target, closest
    ):
        if head is None:
            return closest
        if abs(target - closest) > abs(target - head.value):
            closest = head.value
        if target < head.value:
            return self.binary_search_tree_find_closest_value_recursive_helper(
                head.left, target, closest
            )
        elif target > head.value:
            return self.binary_search_tree_find_closest_value_recursive_helper(
                head.right, target, closest
            )
        else:
            return closest
