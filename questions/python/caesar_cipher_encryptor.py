class Solution:
    def caesar_cipher_encryptor(self, string, key):  # time O(n), space O(n)
        new_letters = []
        new_key = key % 26
        for char in string:
            if ord(char) + new_key > ord("z"):
                new_letters.append(chr(ord(char) - 26 + new_key))
            else:
                new_letters.append(chr(ord(char) + new_key))

        return "".join(new_letters)
