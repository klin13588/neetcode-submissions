class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longestStreak = 1

        for num in nums:
            streak = 1
            tmp = num + 1
            while (tmp in numSet):
                streak +=1
                tmp +=1

            longestStreak = max(longestStreak, streak)
        return longestStreak

      