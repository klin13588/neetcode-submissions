class Solution(object):
    def maxArea(self, height):
        '''
        l * w

        length = min(l,r)

        width = left index - right index
        
        '''

        L, R = 0, len(height)-1
        bestArea = 0
        while L < R:
            length = min(height[L], height[R])
            width = R - L

            bestArea = max(bestArea, length * width)

            if height[R] > height[L]:
                L += 1
            else:
                R -= 1
        return bestArea
        





        