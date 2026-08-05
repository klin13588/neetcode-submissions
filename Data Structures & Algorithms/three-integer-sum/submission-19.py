'''
Input: nums = [-1,-1,-1,0,2,2]
                i     l   r

'''

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            L, R = i + 1, len(nums) - 1

            while L < R:
                total = nums[L] + nums[R] + nums[i]

                if total > 0:
                    R -= 1
                elif total < 0:
                    L += 1
                else:
                    res.append([nums[L],nums[R],nums[i]])
                    L += 1
                    R -=1

                    while L < R and nums[R] == nums[R + 1]:
                        R -= 1
        return res