class Solution:
    def is_monotonic(self, array): # time O(n), space O(1)
        is_monotonic_increasing = True
        is_monotonic_decreasing = True
        for index in range(1, len(array)):
            if array[index] < array[index - 1]:
                is_monotonic_increasing = False
            elif array[index] > array[index - 1]:
                is_monotonic_decreasing = False

        return is_monotonic_increasing or is_monotonic_decreasing