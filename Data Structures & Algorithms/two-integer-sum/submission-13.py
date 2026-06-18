class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}

        for index, num in enumerate(nums):
            complement = target - num
            if complement not in hashmap:
                hashmap[num] = index
            else:
                return [hashmap[complement], index]
