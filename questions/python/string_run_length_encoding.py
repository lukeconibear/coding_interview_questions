class Solution:
    def run_length_encoding(self, string):
        encoded_string = []
        counter = 1
        for index in range(1, len(string)):
            if counter == 9 or string[index] != string[index - 1]:
                encoded_string.append(str(counter))
                encoded_string.append(string[index - 1])
                counter = 0

            counter += 1

        encoded_string.append(str(counter))
        encoded_string.append(string[len(string) - 1])

        return "".join(encoded_string)
