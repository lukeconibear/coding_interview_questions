class Solution:
    def longest_peak_length(self, array):  # time O(n), space O(1)
        longest_peak_length = 0
        index = 1
        while index < len(array) - 1:
            is_peak = (
                array[index] > array[index - 1] and array[index] > array[index + 1]
            )
            if not is_peak:
                index += 1
                continue

            left_index = index - 2
            right_index = index + 2
            while left_index >= 0 and array[left_index] < array[left_index + 1]:
                left_index -= 1

            while (
                right_index <= len(array) - 1
                and array[right_index] < array[right_index - 1]
            ):
                right_index += 1

            current_peak_length = right_index - left_index - 1
            longest_peak_length = max(current_peak_length, longest_peak_length)
            index = right_index

        return longest_peak_length
