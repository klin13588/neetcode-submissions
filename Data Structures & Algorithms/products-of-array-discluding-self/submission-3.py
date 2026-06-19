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

        i'm creating a prefix and postfix array and then multiplying them together
        '''

        # prefix = [1] * len(nums)
        # postfix = [1] * len(nums)
        # res = []
        # for i in range(len(nums)-1):
        #     prefix[i+1] = prefix[i] * nums[i]
        
        # for i in range(len(nums)-2, -1, -1):
        #     postfix[i] = postfix[i+1] * nums[i+1]

        # for i in range(len(nums)):
        #     res.append(postfix[i] * prefix[i])
        
        # return res

        n = len(nums)
        res = [1] * n

        prefix = 1

        for i in range(n):
            res[i] = prefix
            prefix *= nums[i]
        
        postfix = 1
        for i in range(n - 1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]
        
        return res
