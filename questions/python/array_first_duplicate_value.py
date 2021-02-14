class Solution:
    def first_duplicate_value(self, array):  # time O(n), space O(n)
        seen_values = set()
        for value in array:
            if value in seen_values:
                return value

            seen_values.add(value)

        return -1
