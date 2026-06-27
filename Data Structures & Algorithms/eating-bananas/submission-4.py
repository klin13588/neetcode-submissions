class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        L, R = 1, max(piles)
        answer = R

        while L <= R:

            mid = (L + R) // 2
            total_hours = 0
            for pile in piles:
                total_hours += math.ceil(pile/mid)
            
            if total_hours > h:
                L = mid + 1
            
            else:
                answer = mid
                R = mid - 1
        
        return answer
                
                
                