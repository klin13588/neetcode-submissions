class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """

        L, R = 0, len(numbers) - 1

        while R > L:
            cur = numbers[L] + numbers[R]

            if cur > target:
                r -=1
            elif cur < target:
                l += 1
            else:
                return [L+1, R+1]
        return []