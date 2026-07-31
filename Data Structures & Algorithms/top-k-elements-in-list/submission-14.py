class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        bucket = [[] for _ in range(len(nums) + 1)]
        res = []

        for num in nums:
            freq[num] = freq.get(num, 0) + 1

        for n, c in freq.items():
            bucket[c].append(n)

        for i in range(len(bucket) - 1, 0, -1):
            for num in bucket[i]:
                res.append(num)

                if len(res) == k:
                    return res