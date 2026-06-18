class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
         seen = {}
         for i, num in enumerate(nums):
            j = target - nums[i]
            if j in seen:
                return [seen[j], i]
            seen[num] = i

