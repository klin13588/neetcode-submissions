class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        '''
        Instead of checking every possible subarray, keep track of sums we have seen before

        We keep track of a prefixSum which means the sum from the start of the array
        up to the current position 

        previousSum = currentSum - k

        We are checking if we have seen a previous prefix sum that would make the subarray
        bewteen then and now equal to k?

        So at each index 
        1. we add cur num to curSum
        2. compute needed = curSum - k
        3. if needed appeared before, those are valid subarrays -> add to res
        4. store curSum
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


