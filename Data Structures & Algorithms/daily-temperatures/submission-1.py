class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        '''
        stack = 30

        38 > stack[-1]30 yes -> prev index = stack.pop()
        res[prev_index] = i-prev_index

        stack.append(i)
        '''

        res = [0] * len(temperatures)

        stack = []

        for i,temp in enumerate(temperatures):
            while stack and  temp > temperatures[stack[-1]]:
                prev_index = stack.pop()
                res[prev_index] = i - prev_index
            stack.append(i)
        return res