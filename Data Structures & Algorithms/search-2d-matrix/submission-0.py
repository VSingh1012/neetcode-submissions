class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        # matrix=[[1,3,5,7],[10,11,16,20],[23,30,34,60]]
        # target=3
        
        l, r = 0, len(matrix) - 1

        while l <= r:
            m = l + ((r - l) // 2)

            if target > matrix[m][-1]: 
                l = m + 1
            elif target < matrix[m][0]:
                r = m - 1 
            else:
                return self.rowSearch(matrix[m], target)

        
        return False



    


    def rowSearch(self, inner_matrix, target):
        l, r = 0, len(inner_matrix) - 1

        while l <= r:
            m = l + ((r - l) // 2)

            if target > inner_matrix[m]:
                l = m + 1
            elif target < inner_matrix[m]:
                r = m - 1
            else:
                return True


        return False
        

