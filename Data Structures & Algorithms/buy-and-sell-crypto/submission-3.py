class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        '''
        so we have a L and R pointer
        best var to hold the best profit we see in prices arr

        L = 0

        for R in range(L + 1, len(nums)): R will be one ahead of L all the way to the end of prices
            if prices[R] > prices[L]: only if the right price is > left price which means a we made a profit
                best = max(best, prices[R] - prices[L]) calculate the profit and pick the best one
            else: we are losing profit on this pair
                L = R we move our left pointer to where R is 
        return best
        '''

        L = 0
        best = 0

        for R in range(L + 1, len(prices)):
            if prices[R] > prices[L]:
                best = max(best, prices[R] - prices[L])
            else:
                L = R
        return best

            