class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m= len(matrix)
        n=len(matrix[0])
        
        if m == 0:
            return False
        left =0
        right= m*n -1
        
        while left <=right:
            pivot_idx= (left+right)//2
            pivotele = matrix[pivot_idx//n][pivot_idx%n]
            
            if pivotele == target:
                return True
            else:
                if target < pivotele:
                    right= pivot_idx-1
                else:
                    left = pivot_idx+1
        return False
