class Solution:
    def insertion_sort(self, array):
        for index1 in range(1, len(array)):
            index2 = index1
            while index2 > 0 and array[index2] < array[index2 - 1]:
                array[index2], array[index2 - 1] = array[index2 - 1], array[index2]
                index2 -= 1

        return array