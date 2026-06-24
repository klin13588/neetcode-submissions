class Solution:
    '''
    res = exactly one pair of indices i and j , return with smaller index first

    seen = {} loop through nums if not in seen add to this dict

    while looping we compute the complement by subtracting target - i and if complement is in seen

    return the pair

    2,7 t = 9

    9-2 = 7

    2:0

    9-7 = 2

    yes 2 is in seen




    '''
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for i, num in enumerate(nums):
            complement = target - num

            if complement in seen:
                return [seen[complement], i]
            seen[num] = i

