class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        '''
        nums = [2,-1,1,2]
        prefixSum = [2, 1, 2, 4]

        2 + -1 = 1

        needed = 1 - 2 = -1

        if needed in 
        '''

        res = 0
        curSum = 0
        prefixSums = {0 : 1}

        for n in nums:
            curSum += n
            needed = curSum - k

            res += prefixSums.get(needed, 0)
            prefixSums[curSum] = prefixSums.get(curSum,0) + 1
        return res


