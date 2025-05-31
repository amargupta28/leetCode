class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        dp=[None]*(amount+1)
        dp[0]=0
        for i in range(1,len(dp)):
            dp[i] =float('inf')
        
        for i in range(1,amount+1):
            for j in coins:
                if i-j >=0:
                    dp[i] = min(dp[i],dp[i-j]+1)
        return -1 if dp[-1] == float('inf') else dp[-1]
