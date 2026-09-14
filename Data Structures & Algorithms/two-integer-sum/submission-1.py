class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        difdit = {} #val : index

        #for i, n in enumerate(nums) - access index and values without using nums[i] but only n
        for i in range(len(nums)):
            difference = target - nums[i]
            if difference in difdit:
                return [difdit[difference], i]
            else:
                difdit[nums[i]] = i

