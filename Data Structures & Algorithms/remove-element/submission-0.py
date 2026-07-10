class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        '''
        2 2 3 2 3
            l
              r
        l,r pointer where the r pointer is scanning for num that isn't val
            if nums[r] == val:
                we move l = r
                r += 1
            else:
                nums[l] = nums[r]
        '''
        l = 0

        for r in range(len(nums)):
            if nums[r] != val:
                nums[l] = nums[r]
                l += 1
        return l + 1
