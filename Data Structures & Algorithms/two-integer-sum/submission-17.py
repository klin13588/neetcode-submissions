class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for num, i in enumerate(nums):
            diff = target - num

            if diff in seen:
                return [seen[num],i]
            seen[num] = i 
                        
