class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        combination= m+n-2
        t=m-1
        res=1
        for i in range(1,t+1):
            res=res*(combination-t+i)/i
        return res
    
    #Recursion 
    #DP
    #combinations
