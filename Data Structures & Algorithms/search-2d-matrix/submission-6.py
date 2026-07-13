class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        '''
        1. Binary search over the rows to find which row could contain target
            
        2. Binary serach inside that row to find the target

        '''

        top , bottom = 0, len(matrix) - 1
        L, R = 0, len(matrix[0]) - 1

        while top <= bottom:
            row = (top + bottom) // 2

            if target > matrix[row][-1]:
                top = row + 1
            elif target < matrix[row][0]:
                bottom = row - 1
            else:
                break
            
        if not (top <= bottom):
            return False

        row = (top + bottom) // 2
        
        while L <= R:
            mid = (L + R) // 2

            if target > matrix[row][mid]:
                L = mid + 1
            elif target < matrix[row][mid]:
                R = mid - 1
            else:
                return True
        
        return False
        

        