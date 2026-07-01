class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        best = 0
        L = 0

        for R in range(L + 1, len(prices)):
            if prices[R] > prices[L]:
                best = max(best, R-L)
            else:
                L = R
        return best