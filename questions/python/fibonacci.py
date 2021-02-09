class Solution:
    def fib_recursive_brute_force(self, num):  # time O(2^n - as 2 calls to fib n times), space O(n - as n calls on the call stack due to recursion)
        if num == 0 or num == 1:
            return 0
        elif num == 2:
            return 1
        return self.fib_recursive_brute_force(num - 1) + self.fib_recursive_brute_force(num - 2)

    def fib_recursive_cached(self, num, cache={0: 0, 1: 0, 2: 1}):  # time O(n - as 1 call to fib per num), space O(n - from dict / n calls on the call stack due to recursion)
        if num in cache:
            return cache[num]
        else:
            cache[num] = self.fib_recursive_cached(num - 1, cache) + self.fib_recursive_cached(num - 2, cache)
            return cache[num]

    def fib_iterative(self, num):  # time O(n), space O(1)
        if num == 0 or num == 1:
            return 0
        elif num == 2:
            return 1

        previous = 0
        current = 1
        for _ in range(2, num):
            total = current + previous
            previous = current
            current = total

        return total