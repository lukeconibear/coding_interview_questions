class Solution:
    def move_num_to_end(self, array, num_to_move):  # time O(n), space O(1)
        left_index = 0
        right_index = len(array) - 1
        while left_index < right_index:
            while left_index < right_index and array[right_index] == num_to_move:
                right_index -= 1

            if array[left_index] == num_to_move:
                array[left_index], array[right_index] = (
                    array[right_index],
                    array[left_index],
                )

            left_index += 1

        return array
