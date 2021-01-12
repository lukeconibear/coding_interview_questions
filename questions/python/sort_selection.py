class Solution:
    def selection_sort(self, array): # time O(n2), space O(1)
        current_index = 0
        while current_index < len(array) - 1:
            smallest_index = current_index
            for index in range(current_index + 1, len(array)):
                if array[smallest_index] > array[index]:
                    smallest_index = index

            array[current_index], array[smallest_index] = array[smallest_index], array[current_index]
            current_index += 1

        return array