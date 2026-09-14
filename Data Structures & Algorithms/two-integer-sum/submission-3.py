class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dit = {}

        for i, n in enumerate(nums):
            diff = target - n
            if diff in dit:
                return [dit[diff], i]
            else:
                dit[n] = i