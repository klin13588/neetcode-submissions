class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        bucket = [[] for _ in range(len(nums) + 1)]
        res = []

        for num in nums:
            freq[num] = freq.get(num, 0) + 1
        
        for n, c in freq.items():
            bucket[c].append(n)
        
        for count in range(len(bucket) - 1, -1 ,-1):
            for n in bucket[count]:
                res.append(n)

                if len(res) == k:
                    return res