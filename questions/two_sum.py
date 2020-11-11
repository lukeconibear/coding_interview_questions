class Solution:
    def two_sum_naive(self, array, target):  # time O(n^2), space O(1)
        for index1 in range(0, len(array)):
            for index2 in range(1, len(array)):
                if array[index1] + array[index2] == target and index1 != index2:
                    return [index1, index2]

        return []


    def two_sum_cache(self, array, target):  # time O(n), space O(n)
        diffs = {}
        for index, num in enumerate(array):
            diff = target - num
            if diff in diffs:
                return [index, diffs[diff]]
            diffs[num] = index

        return []