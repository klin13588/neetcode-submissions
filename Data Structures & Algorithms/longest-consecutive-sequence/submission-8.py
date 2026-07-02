class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = set(nums)
        best = 0

        for n in res:
            if n-1 not in res:
                length = 1
                current = n
                
                while current + 1 in res:
                    length += 1
                    current += 1

                best = max(best, length)
        return best