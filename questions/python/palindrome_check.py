class Solution:
    def is_palindrome(self, string):
        for index in range(len(string) - 1):
            if string[index] != string[len(string) - 1 - index]:
                return False

        return True
