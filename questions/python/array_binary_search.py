class Solution:
    def binary_search_recursive(self, array, target):  # time O(lgn), space O(lgn)
        return self.binary_search_recursive_helper(array, target, 0, len(array) - 1)

    def binary_search_recursive_helper(self, array, target, left_index, right_index):
        middle_index = (left_index + right_index) // 2
        potential_match = array[middle_index]
        if target == potential_match:
            return middle_index
        elif target < potential_match:
            return self.binary_search_recursive_helper(
                array, target, left_index, middle_index - 1
            )
        else:
            return self.binary_search_recursive_helper(
                array, target, middle_index + 1, right_index
            )

        return -1

    def binary_search_iterative(self, array, target):  # time O(lgn), space O(1)
        return self.binary_search_iterative_helper(array, target, 0, len(array) - 1)

    def binary_search_iterative_helper(self, array, target, left_index, right_index):
        while left_index <= right_index:
            middle_index = (left_index + right_index) // 2
            potential_match = array[middle_index]
            if target == potential_match:
                return middle_index
            elif target < potential_match:
                right_index = middle_index - 1
            else:
                left_index = middle_index + 1

        return -1
