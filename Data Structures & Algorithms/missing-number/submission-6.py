class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums = sorted(nums)
        for i in range(0, len(nums)):
            pos = i
            if nums[i] != i:
                return i
            
        return pos + 1
            
        