import math

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        boxes = [[[False]*10 for _ in range(3)] for _ in range(3)]
        column = [[False]*10 for _ in range(9)]
        row = [[False]*10 for _ in range(9)]

        for i in range (9):
            for j in range(9):
                ele = board[i][j]
                if ele == '.': continue

                ele = int(ele)
                boxRow = i//3
                boxCol = j//3

                if row[i][ele] or column[j][ele] or boxes[boxRow][boxCol][ele]: 
                    return False

                row[i][ele] = True
                column[j][ele] = True
                boxes[boxRow][boxCol][ele] = True

        return True

# Analysis
# Runtime: O(9^2)
