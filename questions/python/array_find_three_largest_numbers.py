class Solution:
    def find_three_largest_numbers_sort(self, array):  # time O(nlgn), space O(1)
        three_largest = [array[0], array[1], array[2]]
        three_largest.sort()
        for num in array[3:]:
            if num > three_largest[2]:
                three_largest[0] = three_largest[1]
                three_largest[1] = three_largest[2]
                three_largest[2] = num
            elif num > three_largest[1]:
                three_largest[0] = three_largest[1]
                three_largest[1] = num
            elif num > three_largest[0]:
                three_largest[0] = num

        return three_largest

    def find_three_largest_numbers_no_sort(self, array):  # time O(n), space O(1)
        three_largest = [None, None, None]
        for num in array:
            self.update_largest(three_largest, num)

        return three_largest

    def update_largest(self, three_largest, num):
        if three_largest[2] is None or num > three_largest[2]:
            self.shift_and_update(three_largest, num, 2)
        elif three_largest[1] is None or num > three_largest[1]:
            self.shift_and_update(three_largest, num, 1)
        elif three_largest[0] is None or num > three_largest[0]:
            self.shift_and_update(three_largest, num, 0)

    def shift_and_update(self, array, num, current_index):
        for index in range(current_index + 1):
            if index == current_index:
                array[index] = num
            else:
                array[index] = array[index + 1]
