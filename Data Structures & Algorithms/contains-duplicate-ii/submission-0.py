class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
       
        '''
        nums=[1,2,3,1]

        L = 1
        R = 2

        1 != 2 and 0 + 1 < 3

        '''
        window = set()
        L = 0

        for R in range(len(nums)):
            if R-L > k:
                window.remove(nums[L])
                L += 1
            if nums[R] in window:
                return True
            window.add(nums[R])
        return False