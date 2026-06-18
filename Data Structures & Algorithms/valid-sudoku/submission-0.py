class Solution(object):
    def isValidSudoku(self, board):
        for row in board:
            seen = set()
            for num in row:
                if num == ".":
                    continue
                if num in seen:
                    return False
                seen.add(num)
        
        for col in range(9):
            seen = set()
            for row in range(9):
                num = board[row][col]
                if num == ".":
                    continue
                if num in seen:
                    return False
                seen.add(num)

        for row_start in range(0, 9, 3):  # Start of each 3x3 block row
                    for col_start in range(0, 9, 3):  # Start of each 3x3 block column
                        seen = set()
                        for row in range(row_start, row_start + 3):  # Rows in the block
                            for col in range(col_start, col_start + 3):  # Columns in the block
                                num = board[row][col]
                                if num == ".":
                                    continue
                                if num in seen:
                                    return False
                                seen.add(num)
                
        return True