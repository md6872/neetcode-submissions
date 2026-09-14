class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = 0
        new = 0

        for i in range(len(nums)):
            if nums[i] == 1:
                count += 1
                if count > new:
                    new = count
            else:
                count = 0

        return new