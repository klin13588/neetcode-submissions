class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        '''
        we can turn nums into a set? 

        if nums - 1 doesn't exit in this set that means its the beginning and we can check for next
        '''

        res = set(nums)
        best = 0
        for num in res:
            if num -1 not in res:
                length = 1
                current = num

                while current + 1 in res:
                    length += 1
                    current += 1
                    
                best = max(length,best)
        return best
                
        