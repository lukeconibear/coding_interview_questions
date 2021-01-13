class Solution:
    def products(self, array): # time O(n), space O(n)
        total_product = 1
        index_zero = 0
        num_zeros = 0
        result = []

        for index in range(len(array)):
            num = array[index]
            total_product *= num
            if num == 0:
                num_zeros += 1
                index_zero = index

        for index in range(len(array)):
            if total_product == 0:
                result.append(0)
            else:
                result.append(total_product / array[index])

        if num_zeros == 1:
            product_indices = [index for index in range(len(array))]
            del product_indices[index_zero]
            result[index_zero] = 1
            for product_index in product_indices:
                result[index_zero] *= array[product_index]

        return result
