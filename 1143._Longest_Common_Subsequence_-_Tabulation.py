class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        """
        :type text1: str
        :type text2: str
        :rtype: int
        """
        mat=[[None for i in range(len(text2)+1)] for j in range(len(text1)+1)]
        
        for j in range(len(mat[0])):
            mat[0][j] =0
        for i in range(len(mat)):
            mat[i][0] = 0
        
        for i in range(1,len(text1)+1):
            for j in range(1,len(text2)+1):
                # print(i,j)
                if text1[i-1] == text2[j-1]:
                    mat[i][j] =1+ mat[i-1][j-1]
                else:
                    mat[i][j] = max(mat[i-1][j],mat[i][j-1])
                # print(mat,i,j)
        return mat[i][j]
