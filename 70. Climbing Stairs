class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 2:
            return n
        dp = [None]*(n+1)
        dp[0]=1
        dp[1] =1
        for i in range(2,len(dp)):
            dp[i] =dp[i-1]+dp[i-2]
        print(dp)
        return dp[n]
