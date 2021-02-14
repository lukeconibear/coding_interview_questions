class Solution:
    def is_valid_subsequence(self, array, sequence):  # time O(n), space O(1)
        index_sequence = 0
        for value in array:
            if index_sequence == len(sequence):
                break
            if value == sequence[index_sequence]:
                index_sequence += 1

        return index_sequence == len(sequence)

    def is_valid_subsequence_alternative(
        self, array, sequence
    ):  # time O(n), space O(1)
        index_array = 0
        index_sequence = 0
        while index_array < len(array) and index_sequence < len(sequence):
            if array[index_array] == sequence[index_sequence]:
                index_sequence += 1

            index_array += 1

        return index_sequence == len(sequence)
