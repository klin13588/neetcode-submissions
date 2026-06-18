class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        '''
        [2,2,2,2,5,5,5,8]
         ^ 
        starting from the beginning of the list for loop 
        through each elememt within the array
        '''

        l = 0
        res = 0
        for i in range(0, len(arr) - k + 1):
            subSum = 0
            for j in range(i, i + k):
                subSum += arr[j]
            
            if subSum / k >= threshold:
                res += 1
        
        return res

        