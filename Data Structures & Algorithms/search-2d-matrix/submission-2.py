class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        '''
        we have a for loop that looks at the end of each row matrix[i][-1]
        1. if target > matrix[i][-1] that means i need to try next row
        2. else this row can only contain or not contain no other row can
        '''

        for row in range(len(matrix)):
            if target > matrix[row][-1]:
                continue
            else:
                #binary search
                L, R = 0, len(matrix[row]) - 1

                while L <= R:
                    mid = (L + R) // 2

                    if target > matrix[row][mid]:
                        L = mid + 1
                    elif target < matrix[row][mid]:
                        R = mid - 1
                    else:
                        return True
        return False


