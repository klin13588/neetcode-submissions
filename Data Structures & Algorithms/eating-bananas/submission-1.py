class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        '''
        Binary search over answer range.

        L = 1
        R = max(piles)

        For each mid speed:
            Calculate how many total hours it takes to eat all piles.

            If total_hours > h:
                speed is too slow
                need to increase speed
                L = mid + 1

            Else:
                speed works
                store answer
                try to find a smaller valid speed
                R = mid - 1
        '''

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

