class Solution:
    def three_number_sum(self, array, target_sum): # time O(n2), space O(n)
        array.sort()
        triplets = []
        for index in range(len(array) - 2):
            left_index = index + 1
            right_index = len(array) - 1
            while left_index < right_index:
                current_sum = array[index] + array[left_index] + array[right_index]
                if current_sum == target_sum:
                    triplets.append([array[index], array[left_index], array[right_index]])
                    left_index += 1
                    right_index -= 1
                elif current_sum < target_sum:
                    left_index += 1
                elif current_sum > target_sum:
                    right_index -= 1

        return triplets
