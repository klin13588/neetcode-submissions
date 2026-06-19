class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        '''
        [1, 2, 4, 6]

        prefix = [1, 1, 2, 8] 

        postfix = [48, 24, 6, 1]

        prefix[0] = 1
        prefix[1] = prefix[0] * nums[0] = 1
        prefix[2] = prefix[1] * nums[1] = 2
        prefix[3] = prefix[2] * nums[2] = 8   

        postfix[3] = 1
        postfix[2] = postfix[3] * nums[3]      
        '''

        prefix = [1] * len(nums)
        postfix = [1] * len(nums)
        res = []
        for i in range(len(nums)-1):
            prefix[i+1] = prefix[i] * nums[i]
        
        for i in range(len(nums)-2, -1, -1):
            postfix[i] = postfix[i+1] * nums[i+1]

        for i in range(len(nums)):
            res.append(postfix[i] * prefix[i])
        
        return res
