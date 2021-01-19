class Solution:
    def find_smallest_difference(self, array_one, array_two): # time O(nlgn + mlgm), space O(1)
        array_one.sort()
        array_two.sort()
        index_one = 0
        index_two = 0
        smallest_difference = float('inf')
        while index_one < len(array_one) and index_two < len(array_two):
            num_one = array_one[index_one]
            num_two = array_two[index_two]
            current_difference = abs(num_one - num_two)
            if num_one < num_two:
                index_one += 1
            elif num_one > num_two:
                index_two += 1
            else:
                return [num_one, num_two]

            if current_difference < smallest_difference:
                smallest_difference = current_difference
                smallest_pair = [num_one, num_two]

        return smallest_pair
