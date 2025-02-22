class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # to save space, use bitmask
        # 0: number not exist 
        # 1: number exists

        # each ele represents a row / col
        rows = [0] * 9
        cols = [0] * 9

        # boxes[0][0] is the first square/box
        boxes = [[0] * 3 for _ in range(3)]
        print(boxes)

        for row in range(9):
            for col in range(9):
                if board[row][col]  == ".": continue
                ele = int(board[row][col])

                if (1 << int(ele)) & rows[row]: return False
                if (1 << int(ele)) & cols[col]: return False
                if (1 << int(ele)) & boxes[row//3][col//3]: return False

                rows[row] |= (1 << int(ele))
                cols[col] |= (1 << int(ele))
                boxes[row//3][col//3] |= (1 << int(ele))             

        return True