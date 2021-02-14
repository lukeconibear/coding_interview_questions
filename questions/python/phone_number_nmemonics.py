class Solution:
    def phone_number_mnemonics(
        self, phone_number
    ):  # time O(4^n * n), space O(4^n * n) - 4^n as could have '999' where 4 chars for each digit, recursively called 3 times
        results = []
        current_result = ["0"] * len(phone_number)
        self.phone_number_mnemonics_helper(0, phone_number, current_result, results)
        return results

    def phone_number_mnemonics_helper(
        self, index, phone_number, current_result, results
    ):
        if index == len(phone_number):
            results.append(
                "".join(current_result)
            )  # where the O(* n) comes from in the time complexity
        else:
            digit = phone_number[index]
            chars = DIGIT_CHARS[digit]
            for char in chars:
                current_result[index] = char
                self.phone_number_mnemonics_helper(
                    index + 1, phone_number, current_result, results
                )


DIGIT_CHARS = {
    "0": ["0"],
    "1": ["1"],
    "2": ["a", "b", "c"],
    "3": ["d", "e", "f"],
    "4": ["g", "h", "i"],
    "5": ["j", "k", "l"],
    "6": ["m", "n", "o"],
    "7": ["p", "q", "r", "s"],
    "8": ["t", "u", "v"],
    "9": ["w", "x", "y", "z"],
}
