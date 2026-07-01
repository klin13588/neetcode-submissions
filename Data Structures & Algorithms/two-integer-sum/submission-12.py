class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        subtract = 0
        if len(nums) == 2:
            return [0,1]
        for index, num in enumerate(nums):
            subtract = target - num
            if subtract in nums:
                return [index, nums.index(subtract)]