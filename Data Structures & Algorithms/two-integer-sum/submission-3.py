class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 2:
            return [0,1]
            
        for i in range(0, len(nums)-1):
            j = target - nums[i]
            if j in nums and nums.index(j) != i:
                return [i, nums.index(j)]
        