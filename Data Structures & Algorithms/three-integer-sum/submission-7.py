class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        '''
        the for loop only needs to go in range(len(nums) - 2) as we already have L and R pointer 
        can't go into last two elements

        there are two places for duplicates 
        1. duplicate i values 
            if i > 0 and nums[i] == nums[i-1]:
                continue
        2. L or R being dulpicate in our case we only increment L 
            while L < R and nums[L] == nums[L-1]:
                L += 1
        '''
        nums.sort()
        res = []

        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i-1]:
                continue

            L, R = i+1, len(nums) - 1

            while L < R:
                if nums[L] + nums[R] + nums[i] > 0:
                    R -=1
                elif  nums[L] + nums[R] + nums[i] < 0:
                    L += 1
                else:
                    res.append([nums[L], nums[R], nums[i]])
                    L += 1
                    R -= 1

                    while L < R and nums[L] == nums[L-1]:
                        L +=1 
        return res
                



        