class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        l, r = 0, len(matrix) - 1

        while l <= r:
            m = (l + r) // 2

            if target > matrix[m][-1]:
                l = m + 1
            elif target < matrix[m][0]:
                r = m - 1
            else:
                return self.isInMatrix(matrix[m], target)

        return False
    
    
    def isInMatrix(self, submatrix, target):

        # regular binary search algorithm

        l, r = 0, len(submatrix) - 1

        while l <= r:
            
            m = (l + r) // 2 

            if target == submatrix[m]:
                return True
            elif target > submatrix[m]:
                l = m + 1
            else:
                r = m - 1

        return False

