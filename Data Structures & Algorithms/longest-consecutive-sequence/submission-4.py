class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        '''
        
        Input: nums = [0,3,2,5,4,6,1,1]

        Output: 7

        nums=[2,20,4,10,3,4,5]

        use a set on nums then we want to check -1 and +1 if -1 doesn't exist that is our begining
        '''

        nums_set = set(nums)
        best = 0
        for num in nums_set:
            if num - 1 not in nums_set:
                length = 1
                current = num

                while current + 1 in nums_set:
                    length += 1
                    current += 1
        
                best = max(length,best)
        return best