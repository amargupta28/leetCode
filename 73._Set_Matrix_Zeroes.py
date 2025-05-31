class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        row= [1]*len(matrix)
        col=[1]*len(matrix[0])
        
        for i in range(len(row)):
            for j in range(len(col)):
                if matrix[i][j] == 0:
                    row[i] =0
                    col[j] =0
        for i in range(len(row)):
            if row[i] == 0 :
                for j in range(len(col)):
                    matrix[i][j] = 0
        for j in range(len(col)):
            if col[j] == 0:
                for i in range(len(row)):
                    matrix[i][j] =0
