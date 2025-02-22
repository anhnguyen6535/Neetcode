class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [0] * 9 
        columns = [0] * 9
        boxes = [[0] * 3 for _ in range(3)]

        # boxes = [[0] * 3 for _ in range(3)]
        # boxes[0][0] = 82
        # print(boxes)

        for i in range(9):
            for j in range(9):
                if board[i][j] == '.': continue
                val  = int(board[i][j]) - 1

                if ((1 << val) & rows[i]): 
                    return False
                if ((1 << val) & columns[j]): 
                    return False
                if ((1 << val) & boxes[i//3][j//3]): 
                    return False

                rows[i] |= (1 << val)
                columns[j] |= (1 << val)
                boxes[i//3][j//3] |= (1 << val)
        
        return True





# Time: O(n^2)
# Space: O(n^2)
# class Solution:
#     def isValidSudoku(self, board: List[List[str]]) -> bool:
#         length = 9
#         rows = [[False] * 10 for _ in range (length)]
#         columns = [[False] * 10 for _ in range (length)]
#         boxes = [[[False] * 10 for _ in range(3)] for _ in range(3)]

#         for i in range(length):
#             for j in range(length):
#                 if board[i][j] != ".":
#                     val = int(board[i][j])

#                     if rows[i][val] or columns[j][val]: return False

#                     boxRow = i // 3
#                     boxCol = j // 3
#                     if boxes[boxRow][boxCol][val]: return False

#                     rows[i][val] = True
#                     columns[j][val] = True
#                     boxes[boxRow][boxCol][val] = True          

#         return True
