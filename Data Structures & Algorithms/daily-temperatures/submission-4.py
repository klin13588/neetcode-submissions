class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        '''
        Keep a stack of days that are still waiting for a warmer temp

        Monotonic decreasing stack because the temperatures in the stack are generally decreasing
        When a warmer day appears, it resolves previous colder days

        while the stack isn't empty and cur temp > temp[stack[-1]]:
            pop the index and resolve the day using the index - prev index
            else you append to the stack waiting for a further warmer temp
        '''

        res = [0] * len(temperatures)

        stack = []

        for i,temp in enumerate(temperatures):
            while stack and  temp > temperatures[stack[-1]]:
                prev_index = stack.pop()
                res[prev_index] = i - prev_index
            stack.append(i)
        return res