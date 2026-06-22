class Solution:
    def findMin(self, nums: List[int]) -> int:
        '''
        nums = [3,4,5,6,1,2]

        L, R = 0, len(nums) - 1

        L = 0, 5

        mid = 0 + 5 // 2 = 2

        mid = nums[2] = 5 

        nums[r] = 2

        left = mid + 1 = 2 + 1 = 3

        mid 6 + 2 = 4

        nums[4] = 1

        if nums[mid] > nums[r]: 
            we are in the rotated side of the array or the high part

            so the min might be on the right side of mid
            left = mid + 1
        elif nums[mid] < nums[r]:
            right = mid

        '''
        L, R = 0, len(nums) - 1

        while L < R:
            mid = (L + R) // 2

            if nums[mid] > nums[R]:
                L = mid + 1
            else:
                R = mid
        return nums[R]