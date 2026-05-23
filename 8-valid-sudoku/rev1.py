from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        size = len(board)

        boxes = []

        for box_row in range(0, size, 3):
            for box_col in range(0, size, 3):
                box = []
                for row in range(box_row, box_row + 3):
                    for col in range(box_col, box_col + 3):
                        box.append([row, col])
                boxes.append(box)
        
        rows_horizontal = []
        for row in range(0, size):
            current = []
            
            for col in range(0, size):
                current.append([row, col])
            
            rows_horizontal.append(current)
        
        cols_vertical = []

        for col in range(0, size):
            current = []
        
            for row in range(0, size):
                current.append([row, col])
    
            cols_vertical.append(current)
        
        all_groups = boxes + rows_horizontal + cols_vertical

        for group in all_groups:
            seen = []

            for position in group:
                row = position[0]
                col = position[1]

                number = board[row][col]

                if number != ".":
                    if number in seen:
                        return False
                    else:
                        seen.append(number)
        
        return True
    
sol = Solution()
print(sol.isValidSudoku([["1","2",".",".","3",".",".",".","."],
 ["4",".",".","5",".",".",".",".","."],
 [".","9","8",".",".",".",".",".","3"],
 ["5",".",".",".","6",".",".",".","4"],
 [".",".",".","8",".","3",".",".","5"],
 ["7",".",".",".","2",".",".",".","6"],
 [".",".",".",".",".",".","2",".","."],
 [".",".",".","4","1","9",".",".","8"],
 [".",".",".",".","8",".",".","7","9"]]))