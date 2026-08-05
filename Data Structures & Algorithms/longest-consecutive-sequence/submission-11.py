class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        setOfNums = set(nums)

        best = 0

        for num in nums:
            'nums = [0,3,2,5,4,6,1,1]'
            if num - 1 not in setOfNums:
                length = 1
                cur = num

                while cur + 1 in setOfNums:
                    length += 1
                    cur += 1
                    
                best = max(length, best)
        return best
