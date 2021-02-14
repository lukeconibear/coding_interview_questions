class Solution:
    def non_constructible_change(self, coins):  # time O(nlgn), space O(1)
        coins.sort()

        current_change_made = 0
        for coin in coins:
            if coin > current_change_made + 1:
                return current_change_made + 1

            current_change_made += coin

        return current_change_made + 1
