class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        buyerP = 10001
        maxP=0
        i=0
        l=len(prices)
        while i <l:
            if buyerP > prices[i]:
                buyerP=prices[i]
            else:
                if prices[i] - buyerP > maxP:
                    maxP = prices[i] - buyerP
            i+=1
        return maxP
        
