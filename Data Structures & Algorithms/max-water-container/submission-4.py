class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left = 0
        right = len(height) - 1
        maxArea = 0

        while left < right:
            # l * w
            length = min(height[left], height[right])
            width = right - left
            area = length * width
            maxArea = max(area, maxArea)

            if height[left] < height[right]:
                left += 1
            elif height[right] < height[left]:
                right -= 1
            else:
                left += 1
        return maxArea




        