class Solution:
    def isHappy(self, n: int) -> bool:
        non = []

        def squares(num):
            tot = 0

            for i in range(len(str(num))):
                tot += int(str(num)[i])*int(str(num)[i])

            return tot

        sum = squares(n)

        while sum != 1:
            if sum not in non:
                non.append(sum)
                sum = squares(sum)
            else:
                return False

        return True