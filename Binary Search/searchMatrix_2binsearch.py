# O(logm + log n) = O(log(m*n))

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # first, find the subarray
        # then find the ele in the chosen subarray
        # binary search using first and last ele of mid arr

        leftArr = 0
        rightArr = len(matrix)-1

        while leftArr <= rightArr:
        # for i in range (2):
            midArr = (rightArr + leftArr) // 2
            print(leftArr, rightArr, midArr)

            if target < matrix[midArr][0]:
                print("SMALLER THAN MIDARR", target, matrix[midArr][0])
                rightArr = midArr - 1
            elif target > matrix[midArr][-1]:
                print("LARGER THAN MIDARR", target, matrix[midArr][-1])
                leftArr = midArr + 1
            else:
                print("EQUAL MIDARR", target, matrix[midArr][0], matrix[midArr][-1])
                left = 0
                right = len(matrix[midArr]) - 1

                while left <= right:
                    mid = (right + left) // 2
                    print(left, right, mid)
                    if target < matrix[midArr][mid]:
                        right = mid - 1
                    elif target > matrix[midArr][mid]:
                        left = mid + 1
                    else:
                        return True
                return False
        
        return False