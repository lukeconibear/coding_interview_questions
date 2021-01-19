class Solution:
    def two_sum_brute_force(self, array, target):  # time O(n^2), space O(1)
        for index_one in range(len(array)):
            for index_two in range(index_one + 1, len(array)):
                if array[index_one] + array[index_two] == target and index_one != index_two:
                    return [index_one, index_two]

        return []

    def two_sum_cache(self, array, target):  # time O(n), space O(n)
        diffs = {}
        for index, num in enumerate(array):
            diff = target - num
            if diff in diffs:
                return [index, diffs[diff]]
            diffs[num] = index

        return []
