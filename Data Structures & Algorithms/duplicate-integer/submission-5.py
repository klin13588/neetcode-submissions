class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        x = set()

        for num in nums:
            if num in x:
                return False
            x.add(num)
        return True
            