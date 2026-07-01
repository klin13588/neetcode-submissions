class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        subtract = 0
        for index, num in enumerate(nums):
            subtract = target - num
            if subtract in nums:
                return [index, nums.index(subtract)]