class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        L, R = 1, max(piles)
        answer = R

        while L <= R:
            mid = (L + R) // 2
            total = 0

            for pile in piles:
                total += math.ceil(pile/mid)

                if total > h:
                    mid = L + 1
                else:
                    answer = mid
                    mid = R - 1
        
        return answer