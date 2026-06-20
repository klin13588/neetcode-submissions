class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        '''
        sort

        then we have two cases where we have identical 

        one is for i 

        the other is for L being the same as previous L-1

        [-1,0,1,2,-1,-4]

        -1 -1 0 1 2 -4
        '''

        nums.sort()
        res = []
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i-1]:
                continue

            L, R = i + 1, len(nums) - 1

            while L < R: 
                if nums[L] + nums[R] + nums[i] > 0:
                    R -= 1
                elif nums[L] + nums[R] + nums[i] < 0:
                    L += 1
                else:
                    res.append([nums[L], nums[R], nums[i]])
                    L += 1
                    R -= 1

                    while L < R and nums[L] == nums[L-1]:
                        L += 1
        return res
                
            