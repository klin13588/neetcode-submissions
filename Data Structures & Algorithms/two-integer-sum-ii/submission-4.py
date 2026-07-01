class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        '''
        L, R pointer that checks if L + R is > target then we need to decrement R by -1 
        because the smallest value + biggest value is larger than target this means even if we 
        increment smallest by +1 it will always be bigger than target vice versa...
        '''

        L, R = 0, len(numbers) - 1

        while L < R:
            if numbers[L] + numbers[R] > target:
                R -= 1
            elif numbers[L] + numbers[R] < target:
                L += 1
            else:
                return [numbers[L],numbers[R]]