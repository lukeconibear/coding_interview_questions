class Solution:
    def bubble_sort(self, array): # time O(average = n2, best = n), space O(1)
        is_sorted = False
        counter = 0
        while not is_sorted:
            is_sorted = True
            for index in range(len(array) - 1 - counter):
                if array[index] > array[index + 1]:
                    array[index], array[index + 1] = array[index + 1], array[index]
                    is_sorted = False

            counter += 1

        return array