class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        res = []
        for i in nums:
            count[i] = 1 + count.get(i,0)

        temp = []
        for key, value in count.items():
            temp.append([value,key])
        temp.sort()
        for i in range(k):
            res.append(temp.pop()[1])
        return res