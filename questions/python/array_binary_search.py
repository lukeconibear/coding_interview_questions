class Solution:
    def binary_search_recursive(self, array, target): # time O(lgn), space O(lgn)
        return self.binary_search_recursive_helper(array, target, 0, len(array) - 1)

    def binary_search_recursive_helper(self, array, target, left, right):
        middle = (left + right) // 2
        potential_match = array[middle]
        if target == potential_match:
            return middle
        elif target < potential_match:
            return self.binary_search_recursive_helper(array, target, left, middle - 1)
        else:
            return self.binary_search_recursive_helper(array, target, middle + 1, right)

        return -1

    def binary_search_iterative(self, array, target): # time O(lgn), space O(1)
        return self.binary_search_iterative_helper(array, target, 0, len(array) - 1)

    def binary_search_iterative_helper(self, array, target, left, right):
        while left <= right:
            middle = (left + right) // 2
            potential_match = array[middle]
            if target == potential_match:
                return middle
            elif target < potential_match:
                right = middle - 1
            else:
                left = middle + 1

        return -1
