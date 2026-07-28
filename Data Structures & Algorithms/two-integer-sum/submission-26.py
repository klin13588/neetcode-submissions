
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        table = {}
      
        for num in range(len(nums)):
            complementary = target - nums[num]
            if complementary in table:
                return [table[complementary], num]
        
            table[nums[num]] = num