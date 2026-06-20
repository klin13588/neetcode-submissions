class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        '''
         [1,1,2,3,4]
            l r 
          1,2,3,4,2
                l r 
          if l == r 
            += 1
            += 1
          else:
            nums[l] = nums[r]
            l += 1
            r += 1
        '''
        if not nums:
            return 0
        L = 1

        for R in range(1, len(nums)):
            if nums[R] == nums[R-1]:
                continue
            else:
                nums[L] = nums[R]
                L += 1
        return L
