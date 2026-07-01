class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        res = []

        for i in range(0, len(nums)):
            count[nums[i]] = 1 + count.get(nums[i],0)
            if count[nums[i]] == k:
                res.append(nums[i])
        return res