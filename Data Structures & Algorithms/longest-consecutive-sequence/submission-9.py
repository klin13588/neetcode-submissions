class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = set(nums)
        best = 0

        for num in nums:
            if num - 1 not in res:
                length = 1
                cur = num 
                while cur + 1 in res:
                    length += 1
                    cur += 1
                
                best = max(best, length)
        return best
        