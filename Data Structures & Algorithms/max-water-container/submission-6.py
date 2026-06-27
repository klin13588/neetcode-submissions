class Solution:
    def maxArea(self, heights: List[int]) -> int:
        L,R = 0, len(heights) - 1
        bestArea = 0

        while L < R:
            length = min(heights[L], heights[R])
            width = R - L
            bestArea = max(bestArea, length * width)

            if heights[L] > heights[R]:
                R -= 1
            else:
                L += 1
        return bestArea


                

