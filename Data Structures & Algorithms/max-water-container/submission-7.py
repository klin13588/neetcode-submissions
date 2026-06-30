class Solution:
    def maxArea(self, heights: List[int]) -> int:
        L, R = 0, len(heights) - 1
        maxAmount = 0

        while L < R:
            length = min(heights[L], heights[R])
            width = R - L
            maxAmount = max(maxAmount, length * width)

            if heights[L] > heights[R]:
                R -=1
            else:
                L += 1
        return maxAmount