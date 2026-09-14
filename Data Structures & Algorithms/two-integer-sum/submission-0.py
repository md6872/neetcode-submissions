class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        difdit = {} #val : index

        for i in range(len(nums)):
            difference = target - nums[i]
            if difference in difdit:
                return [difdit[difference], i]
            else:
                difdit[nums[i]] = i

