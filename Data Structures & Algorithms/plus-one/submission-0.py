class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        string = ""

        for i in range(len(digits)):
            string += str(digits[i])

        num = int(string)
        string = str(num+1)
        new_list = []

        for i in range(len(string)):
            new_list.append(string[i])

        return new_list