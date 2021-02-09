class Solution:
    def max_subset_sum_no_adjacent(self, array): # time O(n), space O(1)
        if len(array) == 0:
            return 0
        elif len(array) == 1:
            return array[0]
        else:
            prevprev = array[0]
            prev = max(array[0], array[1])
            for index in range(2, len(array)):
                current = max(prev, prevprev + array[index])
                prevprev = prev
                prev = current

        return prev