class Solution:
    def insertion_sort(self, array):
        for index_one in range(1, len(array)):
            index_two = index_one
            while index_two > 0 and array[index_two] < array[index_two - 1]:
                array[index_two], array[index_two - 1] = array[index_two - 1], array[index_two]
                index_two -= 1

        return array