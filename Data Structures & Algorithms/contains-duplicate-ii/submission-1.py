class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        '''
        so we have two pointers and a window (set)

        L pointer is set at 0

        R pointer is going to scan all the way to the end of nums

        for r in range(len(nums)):
            if r - l > k : this is to check abs(i - j) <= k
                window.remove(nums[L]) we move our window right and remove the leftmost element
                l += 1  moving our window right

            if nums[R] in window:
                return True

            If we are here this means that we can keep increasing our window size have not found a duplicate yet 
            window.add(nums[R])
        return False

        O(n) time complexity
        O(1) space

        '''

        window = set()

        L = 0

        for R in range(len(nums)):
            if R - L > k:
                window.remove(nums[L])
                L += 1
            
            if nums[R] in window:
                return True
            
            window.add(nums[R])
        return False