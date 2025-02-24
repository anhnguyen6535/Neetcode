# O(log(m*n))
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # treat the matrix as one arr with m*n elements

        N_ROWS, N_COLS = len(matrix), len(matrix[0])
        left, right = 0, N_ROWS * N_COLS -1

        while left <= right:
            mid = (right + left) // 2

            row = mid //  N_COLS 
            col = mid %  N_COLS 

            if target < matrix[row][col]:
                right = mid - 1
            elif target > matrix[row][col]:
                left = mid + 1
            else:
                return True

        return False 