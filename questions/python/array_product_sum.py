class Solution:
    def product_sum(self, array, multiplier=1): # time O(n), space O(depth of special array)
        total = 0
        for item in array:
            if type(item) is list:
                total += self.product_sum(item, multiplier + 1)
            else:
                total += item

        return total * multiplier