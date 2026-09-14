class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        map = {}
        tot = 1

        for i in range(len(nums)):
            if nums[i] in map:
                map[nums[i]] = tot + 1
            else:
                map[nums[i]] = 1

        num = [key for key, val in map.items() if val == 1]

        return num[0]
