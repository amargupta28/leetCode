class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if len(matrix) == 0  and len(matrix[0]) == 0:
            return False
        
        row= len(matrix)
        col = len(matrix[0])
        
        r,c = row-1, 0
        
        while c< col and r >=0:
            if matrix[r][c] > target:
                r-=1
            elif matrix[r][c] < target:
                c+=1
            else:
                return True
        return False
