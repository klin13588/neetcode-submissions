class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0 
            
        L = 1

        for R in range(1, len(nums)):
            if nums[L] == nums[R]:
                continue
            else:
                nums[L] = nums[R]
                L += 1
        return L 