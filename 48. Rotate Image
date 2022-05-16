class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        for i in range(len(matrix)):
            for j in range(i,len(matrix[0])):
                matrix[i][j],matrix[j][i] = matrix[j][i],matrix[i][j]
        for i in range(len(matrix)):
            j=0
            k=len(matrix[i])-1
            while j <k:
                matrix[i][j] , matrix[i][k] = matrix[i][k],matrix[i][j]
                j+=1
                k-=1
