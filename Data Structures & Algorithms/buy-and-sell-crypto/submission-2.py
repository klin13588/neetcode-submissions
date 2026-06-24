class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        L = 0 
        best = 0

        for R in range(L + 1, len(prices)):
            if prices[R] > prices[L]:
                best = max(best, prices[R] - prices[L])
            else:
                L = R
        return best