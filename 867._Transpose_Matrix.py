class Solution(object):
    def transpose(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        row= len(matrix)
        col= len(matrix[0])
        temp=[[None for i in range(row)] for j in range(col)]
        print(temp)
        for i in range(col):
            for j in range(row):
                temp[i][j]=matrix[j][i]
        return temp
